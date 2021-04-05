from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Mechanic, Brand


def all_mechanics(request):
    # View to show all available mechanics

    mechanics = Mechanic.objects.all()
    query = None
    brands = None

# This is from the products filtering and searching lessons and is NOT WORKING correctly, this may be due to the disambiguation between primary_car_brand and brand which
# was used as the foreign key identifier. Although the Botique Ado info is set up in the same manner.

    if request.GET:
        if 'brand' in request.GET:
            brands = request.GET[brand].split[',']
            mechanics = mechanics.filter(brand__name__in=brands)
            brands = Brand.objects.filter(name__in=brands)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(mechanic_name__icontains=query) | Q(primary_car_brand__icontains=query)
            mechanics = mechanics.filter(queries)

    context = {
        'mechanics': mechanics,
        'search_term': query,
        'current_brands': brands,
    }

    return render(request, 'mechanics/mechanics.html', context)


def mechanic_detail(request, mechanic_id):
    # View to show mechanic details

    mechanic = get_object_or_404(Mechanic, pk=mechanic_id)

    context = {
        'mechanic': mechanic,
    }

    return render(request, 'mechanics/mechanic_detail.html', context)
