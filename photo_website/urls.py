"""photo_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from accounts import views as accounts_views
from home import views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from products import views as product_views
from django.contrib.auth import views as auth_views
from django.views.static import serve
from settings.base import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.get_index, name='home'),
    url(r'^gallery/$', views.get_gallery),
    url(r'^products/$', product_views.all_products),
    url(r'', include('blog.urls')),
    # accounts Authentication Url's
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    #paypall url's

    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),

    url('', include('contact.urls')),
    url(r'', include('blog.urls')),

    # reset password ulr

    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),






]



