from django.shortcuts import render, get_object_or_404
from .models import Mechanic


def all_mechanics(request):
    # View to show all available mechanics

    mechanics = Mechanic.objects.all()

    context = {
        'mechanics': mechanics,
    }

    return render(request, 'mechanics/mechanics.html', context)


def mechanic_detail(request, mechanic_id):
    # View to show mechanic details

    mechanic = get_object_or_404(Mechanic, pk=mechanic_id)

    context = {
        'mechanic': mechanic,
    }

    return render(request, 'mechanics/mechanic_detail.html', context)
