# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from django.conf import settings
from products.models import Product
from .models import OrderLineItem
import stripe

# Create your views here.


stripe.api_key = settings.STRIPE_SECRET


def checkout(request):

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.save()
            customer = False
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product
                )
                order_line_item.save()
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")
            try:
                if customer and customer.paid:
                    messages.success(request, "Your payment was successful")
                    request.session['cart'] = {}
                    return redirect(reverse('products'))
                else:
                    messages.error(request, "Unable to take payment")
            except UnboundLocalError:
                messages.error(request, "Unable to create customer")

        else:
            print(payment_form.errors)
            messages.error(request, "Unable to take payment with this card")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout/checkout.html", {'order_form': order_form, 'payment_form': payment_form,
                                             'publishable': settings.STRIPE_PUBLISHABLE})