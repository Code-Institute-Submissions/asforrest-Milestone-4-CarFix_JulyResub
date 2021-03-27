from django.shortcuts import render

# Create your view


def index(request):
    # View to return index page
    return render(request, 'home/index.html')
