from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Subscription, Category
from .forms import SubscriptionForm

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

def add_subscription(request):
    """ Add a subscription to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = SubscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            subscription = form.save()
            messages.success(request, 'Successfully added subscription!')
            return redirect(reverse('subscription_detail', args=[subscription.id]))
        else:
            messages.error(request,
                           ('Failed to add subscription. '
                            'Please ensure the form is valid.'))
    else:
        form = SubscriptionForm()

    template = 'subscriptions/add_subscription.html'
    context = {
        'form': form,
    }

    return render(request, template, context)