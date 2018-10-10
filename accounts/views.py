# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.conf import settings



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                messages.info(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'Registration/register.html', args)


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'registration/profile.html')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.info(request, "You have successfully logged in")
                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('profile'))

            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form, 'next': request.GET.get('next', '')}
    args.update(csrf(request))
    return render(request, 'registration/login.html', args)


def logout(request):
    auth.logout(request)
    messages.info(request, 'You have successfully logged out')
    return redirect(reverse('home'))

def update_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        form = EditProfileForm(instance=request.user)

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'registration/update_profile.html', args)
