from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import register_user as register_user_form
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


def register_user(req):
    if req.user.is_authenticated:
        return redirect(reverse('core:home'))
    if req.method == 'POST':
        form = register_user_form(req.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                req, messages.SUCCESS, "Registration Successfull! verify your email to login")
            return redirect(reverse('customAuth:login'))
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
    if req.user.is_authenticated:
        return redirect(reverse('core:home'))
    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            login(req, user)
            return redirect(reverse('core:home'))

        messages.add_message(
            req, messages.ERROR, 'Incorrect Email Or Password!')

    return render(req, 'customAuth/login.html')


def logout_user(req):
    logout(req)
    return redirect(reverse('core:home'))
