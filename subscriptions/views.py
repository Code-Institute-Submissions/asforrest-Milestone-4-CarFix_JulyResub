from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Subscription
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


@login_required
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


@login_required
def edit_subscription(request, subscription_id):
    """ Edit a subscription in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    subscription = get_object_or_404(Subscription, pk=subscription_id)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, request.FILES, instance=subscription)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated subscription!')
            return redirect(reverse('subscription_detail', args=[Subscription.id]))
        else:
            messages.error(request,
                           ('Failed to update Subscription. '
                            'Please ensure the form is valid.'))
    else:
        form = SubscriptionForm(instance=subscription)
        messages.info(request, f'You are editing {subscription.name}')

    template = 'subscriptions/edit_subscription.html'
    context = {
        'form': form,
        'subscription': subscription,
    }

    return render(request, template, context)


@login_required
def delete_subscription(request, subscription_id):
    """ Delete a subscription from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    subscription = get_object_or_404(Subscription, pk=subscription_id)
    subscription.delete()
    messages.success(request, 'Subscription deleted!')
    return redirect(reverse('subscriptions'))
