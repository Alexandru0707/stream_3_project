# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def get_index(request):
    return render(request, 'home.html')


def get_gallery(request):
    return render(request, 'gallery.html')
