# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages



# Create your views here.


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['alex_boys30@yahoo.com'])

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Success! Thank you for your message.')
            return redirect('email')






    return render(request, "contact/email.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')