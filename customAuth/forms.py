from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model


class register_user(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(register_user, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Phone Number'

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter Password",
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Confirm Password",
    }))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'phone']

    def clean(self):
        cd = self.cleaned_data

        password1 = cd.get("password")
        password2 = cd.get("confirm_password")

        email = cd.get('email')
        phone = cd.get('phone')

        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists in database!")

        if get_user_model().objects.filter(phone=phone).exists():
            raise forms.ValidationError(
                "Phone number already exists in database!")

        if len(password1) < 8:
            raise forms.ValidationError("Password must be 8 chars long")

        if password1 != password2:
            raise forms.ValidationError("Password did not match")

        return cd

    def save(self, commit=True):
        userModel = get_user_model()

        self.cleaned_data.pop('confirm_password')

        user = userModel.objects.create_user(**self.cleaned_data)

        if not user:
            raise forms.ValidationError("Unable To Register User")

        return user
