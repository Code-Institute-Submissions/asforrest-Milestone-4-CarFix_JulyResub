from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your view


def view_cart(request):
    # View to return the contents of the shopping cart page
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    # View to add quantity to the shopping cart
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    # Adjust the quantity of subscriptions
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] += quantity
    else:
        cart.pop[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    try:
        # Adjust the quantity of subscriptions
        cart = request.session.get('cart', {})

        cart.pop[item_id]

        request.session['cart'] = cart
        return HtttpResponse(status=200)
    except Excetpion as e:
        return HtttpResponse(status=500)
