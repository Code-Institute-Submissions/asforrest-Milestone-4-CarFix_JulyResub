from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Mechanic


def all_mechanics(request):
    # View to show all available mechanics

    mechanics = Mechanic.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(mechanic_name__icontains=query) | Q(primary_car_brand__icontains=query)
            mechanics = mechanics.filter(queries)

    context = {
        'mechanics': mechanics,
        'search_term': query,
    }

    return render(request, 'mechanics/mechanics.html', context)


def mechanic_detail(request, mechanic_id):
    # View to show mechanic details

    mechanic = get_object_or_404(Mechanic, pk=mechanic_id)

    context = {
        'mechanic': mechanic,
    }

    return render(request, 'mechanics/mechanic_detail.html', context)
