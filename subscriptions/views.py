from django.shortcuts import render, get_object_or_404
from .models import Subscription


def all_subscriptions(request):
    # View to show subscription comparison

    subscriptions = Subscription.objects.all()

    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'subscriptions/subscriptions.html', context)


def subscription_detail(request, subscription_id):
    # View to show subscription details

    subscription = get_object_or_404(Subscription, pk=subscription_id)

    context = {
        'subscription': subscription,
    }

    return render(request, 'subscriptions/subscription_detail.html', context)
