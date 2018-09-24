from django.contrib import admin
from django.conf.urls import include, url
from contact import views

urlpatterns = [
    url('email/', views.emailView, name='email'),
    url('success/', views.successView, name='success'),
]