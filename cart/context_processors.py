from .cart import Cart
from .views import cart_count

def cart(request):
    return {'cart': Cart(request), 'counts':cart_count(request)}