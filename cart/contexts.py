from django.conf import settings
from django.shortcuts import get_object_or_404
from subscriptions.models import Subscription

def cart_contents(request):

    cart_items = []
    total = 0
    subscription_count = 0
    subscription_credits_count = 0
    total_credits = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        subscription = get_object_or_404(Subscription, pk=item_id)
        total += quantity * subscription.price
        subscription_count += quantity
        # WORKING HERE
        total_credits += quantity * subscription.credits
        subscription_credits_count += quantity
        # WORKING HERE
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'subscription': subscription,

        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'subscription_count': subscription_count,
        'subscription_credits_count': subscription_credits_count,
    }
    return context
