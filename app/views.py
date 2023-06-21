from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Delivery
from .forms import AddAddressViaModelForm
from cart.forms import CartAddProductForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def adress(request):
    return render(request, 'adress.html')


def cart(request):
    return render(request, 'cart.html')


def products(request, category):
    try:
        all_the_products = Product.objects.filter(
            category=category).order_by('-id')
        one_prod = all_the_products[0]
        return render(request, 'products.html', {'all_prod': all_the_products, 'one_pr': one_prod})
    except:
        return render(request, 'products.html')


def product(request, id):
    # try:
    prod = Product.objects.get(id=id)
    one_prod = Product.objects.get(id=id)
    cart_product_form = CartAddProductForm
    return render(request, 'product.html', {'prodid': prod, 'one_pr': one_prod, 'cart_product_form': cart_product_form})
    # except:
    #     response = "There is no product with such an id."
    #     return HttpResponse(response)


def add_model_address(request):

    error = None
    address = AddAddressViaModelForm

    if request.method == 'POST':
        address = AddAddressViaModelForm(request.POST, request.FILES)

        if address.is_valid():
            new_address = address.save(commit=False)
            new_address.user = User.objects.get(pk=request.user.pk)
            new_address.save()
            address.save_m2m()
            return redirect('thank_you')



    a = {'address_new': address, 'error': error}

    try:
        ad_ad = Delivery.objects.filter(user=request.user.email)[0]
        a['ad_ad'] = ad_ad
    except:
        None

    return render(request, 'address.html', a)


def thank_you(request):
    return render(request, 'thank_you.html')


def pre_login(request):
    return render(request, 'pre_login.html')


def del_address(request):
    try:
        del_ad = Delivery.objects.filter(user=request.user.email)[0]
        del_ad.delete()
        return redirect('add_address_new')
    except:
        None
