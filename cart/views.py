# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.



def view_cart(request):
    return render(request, "cart/cart.html")


def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect(reverse('products'))


def adjust_cart(request, id):

    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_cart(request, id):
    cart = request.session.get('cart', {})

    if cart < 0:
        cart[id] = cart
    else:
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


