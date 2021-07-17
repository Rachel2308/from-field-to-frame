from django.conf import settings
from django.shortcuts import get_object_or_404
from art.models import Art

def basket_contents(request):

    basket_items = []
    total = 0
    art_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        art = get_object_or_404(Art, pk=item_id)
        total += quantity * art.price
        art_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'art': art,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = 4.99
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total

    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery = total

    context = {
        'basket_items': basket_items,
        'total': total,
        'art_count': art_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context