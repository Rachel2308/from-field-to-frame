from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from art.models import Art


def view_basket(request):
    """A view to return the basket content page"""

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """A view to add products to shopping basket"""

    art = Art.objects.get(pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, ' Updated quantity of '
                         f'{art.title} to {basket[item_id]}')

    else:
        basket[item_id] = quantity
        messages.success(request, f'{art.title} added to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """A view to adjust the quantity of products in the basket"""

    art = get_object_or_404(Art, pk=item_id)
    basket = request.session.get('basket', {})
    quantity = int(request.POST.get('quantity'))

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, ' Updated quantity of '
                         f'{art.title} to {basket[item_id]}')

    else:
        basket.pop(item.id)
        messages.success(request, f'{art.title} removed from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """A view to remove products from the shopping basket"""

    try:
        art = get_object_or_404(Art, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)

        messages.success(request, f'{art.title} removed from your basket')
        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing {art.title}: {e}')
        return HttpResponse(status=500)
