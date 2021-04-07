from django.conf import settings
from django.shortcuts import get_object_or_404
from subscriptions.models import Subscription

def cart_contents(request):

    cart_items = []
    total = 0
    subscription_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        subscription = get_object_or_404(Subscription, pk=item_id)
        total += quantity * subscription.price
        subscription_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'subscription': subscription,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'subscription_count': subscription_count,
    }
    return context
