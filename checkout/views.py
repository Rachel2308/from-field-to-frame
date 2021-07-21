from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is currently empty")
        return redirect(reverse('art'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IigXGFZqZgLttg6Zzz9ZYlmWL5ZsqfdKxLmV4B0YmdKKRxKkPFzLQoI9Osea0bqXvCsMI3E590ndppJBfl0BECD00rUMy2ylq',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

