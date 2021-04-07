from django.shortcuts import render, redirect

# Create your view


def view_cart(request):
    # View to return the contents of the shopping cart page
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
     # View to add quantity to the shopping bag
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if itemd_id in list(bag.key()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    
    request.session['cart'] = cart
    return redirect(redirect_url)
