from django.shortcuts import render
from .models import Subscription


def all_subscriptions(request):
    # View to show subscription comparison

    subscriptions = Subscription.objects.all()

    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'subscriptions/subscriptions.html', context)
