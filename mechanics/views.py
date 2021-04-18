from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Mechanic, Brand

from django.contrib.auth.decorators import login_required
from .forms import MechanicForm
from profiles.models import UserProfile


def all_mechanics(request):
    # View to show all available mechanics

    mechanics = Mechanic.objects.all()
    query = None
    brands = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                mechanics = mechanics.annotate(lower_name=Lower('name'))
            if sortkey == 'brand':
                sortkey = 'brand__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            mechanics = mechanics.order_by(sortkey)

        if 'brands' in request.GET:
            brands = request.GET['brands'].split(',')
            mechanics = mechanics.filter(brand__name__in=brands)
            brands = Brand.objects.filter(name__in=brands)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('subscriptions'))

            queries = Q(mechanic_name__icontains=query) | Q(primary_car_brand__icontains=query)
            mechanics = mechanics.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'mechanics': mechanics,
        'search_term': query,
        'current_brands': brands,
        'current_sorting': current_sorting,
    }

    return render(request, 'mechanics/mechanics.html', context)


def mechanic_detail(request, mechanic_id):
    # View to show mechanic details

    mechanic = get_object_or_404(Mechanic, pk=mechanic_id)

    context = {
        'mechanic': mechanic,
    }

    return render(request, 'mechanics/mechanic_detail.html', context)

def hire_mechanic(request):
    profile = UserProfile.objects.get(user=request.user)
    profile.total_credits = profile.total_credits - 1
    profile.save()
    return render(request, 'mechanics/hired.html')