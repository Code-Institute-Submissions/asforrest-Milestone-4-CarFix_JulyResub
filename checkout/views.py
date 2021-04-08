from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('subscriptions'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IXHjKHjJQjzesItIzWaWTHYcsYDfOsvFsKLoGNqYr9jQTKpvD40zbIOKJydQLyQLSahXx50FjmsB8uRQh1S4dbM00bhoLcHvu',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
