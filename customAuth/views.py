from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import register_user as register_user_form
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from emailService.email import EmailSender
from tokenService.token import VerificationToken
from django.contrib.sites.shortcuts import get_current_site


def register_user(req):
    """ register new user to the site save the user data in database """
    if req.user.is_authenticated:
        return redirect(reverse('core:home'))
    if req.method == 'POST':
        form = register_user_form(req.POST)
        if form.is_valid():
            user = form.save()
            domain = get_current_site(req)
            EmailSender(domain, 'Verify Email Address',
                        user).account_activation_mail()
            messages.add_message(
                req, messages.SUCCESS, "Registration Successfull! verify your email to login")
            return redirect(reverse('customAuth:signin'))
        else:
            messages.add_message(
                req, messages.ERROR, form.errors.as_data().get('__all__')[0].message)

    else:
        form = register_user_form()

    context = {
        'form': form
    }

    return render(req, 'customAuth/register.html', context=context)


def login_user(req):
    """ verify email and password and let the user login """
    if req.user.is_authenticated:
        return redirect(reverse('core:home'))
    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')

        if get_user_model().objects.is_active_user(email):
            user = authenticate(email=email, password=password)
            if user is not None:
                login(req, user)
                return redirect(reverse('core:home'))
            messages.add_message(req, messages.ERROR,
                                 'Incorrect Email Or Password!')
        else:
            messages.add_message(req, messages.ERROR, 'Account Is Inactive!')

    return render(req, 'customAuth/login.html')


def logout_user(req):
    """ logout a loggedin user """
    if req.user.is_authenticated:
        logout(req)
    return redirect(reverse('core:home'))


def forgot_password(req):
    """ takes email and if email exists then sends a verification link to the user email """
    if req.user.is_authenticated:
        return redirect(reverse('core:home'))

    if req.method == 'POST':
        email = req.POST.get('email')

        if get_user_model().objects.email_exists(email=email):
            # reset password mail sent here
            user = get_user_model().objects.get_by_email(email=email)
            current_site = get_current_site(req)

            EmailSender(current_site, 'Reset Password Link',
                        user).account_reset_password_mail()
            messages.add_message(req, messages.SUCCESS,
                                 'Reset Password mail sent')
        else:
            messages.add_message(req, messages.ERROR,
                                 'Account Does Not Exists')
    return render(req, 'customAuth/forgot-password.html')


def reset_password(req):
    """ verifies the link and resets the password of the user """
    uid = req.session.get('uid')

    if req.method == 'POST':
        password = req.POST.get('password')
        confirmpassword = req.POST.get('confirm_password')

        if len(password) < 8:
            messages.add_message(req, messages.ERROR,
                                 'Password Must Be 8 Chars Long')
            return render(req, 'customAuth/reset-password.html')
        if password and confirmpassword and password != confirmpassword:
            messages.add_message(req, messages.ERROR, 'Password Did Not Match')
            return render(req, 'customAuth/reset-password.html')

        user = get_user_model().objects.get_by_pk(pk=uid)

        if user is not None:
            user.set_password(password)
            user.save()
            messages.add_message(req, messages.SUCCESS, 'Password Updated')
            return redirect(reverse('customAuth:signin'))
        else:
            messages.add_message(req, messages.ERROR, 'User Not Found')

    return render(req, 'customAuth/reset-password.html')


def activate_account(req, uidb64, token):
    """ verify token and activate the give user account """
    try:
        uid = VerificationToken.decode_pk(uidb64)
        userModel = get_user_model()
        user = userModel.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, userModel.DoesNotExist):
        user = None

    if user is not None and VerificationToken.verify_token(user, token):
        user.active = True
        user.save()
        messages.add_message(
            req, messages.SUCCESS, 'Account Activated! Please Login')

    else:
        messages.add_message(req, messages.ERROR, 'Unable To Activate Account')

    return redirect(reverse('customAuth:signin'))


def reset_password_verify(req, uidb64, token):
    """ verify token and reset password """
    try:
        uid = VerificationToken.decode_pk(uidb64)
        userModel = get_user_model()
        user = userModel.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, userModel.DoesNotExist):
        user = None

    if user is not None and VerificationToken.verify_token(user, token):
        req.session['uid'] = uid
        messages.add_message(req, messages.SUCCESS, 'Reset Your Password')
    else:
        messages.add_message(req, messages.ERROR, 'Link Expired')

    return redirect(reverse('customAuth:reset-password'))
