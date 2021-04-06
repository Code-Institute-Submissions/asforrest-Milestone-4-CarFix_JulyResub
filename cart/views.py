from django.shortcuts import render

# Create your view


def view_cart(request):
    # View to return the contents of the shopping cart page
    return render(request, 'cart/cart.html')
