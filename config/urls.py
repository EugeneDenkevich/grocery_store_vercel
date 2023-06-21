"""grocery_store_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include
from django.contrib import admin
from django.urls import path
from app import views as gr_shoping
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', gr_shoping.index, name='index'),
    path('cart/', gr_shoping.cart, name='cart'),
    path('products/<slug:category>', gr_shoping.products, name='products'),
    path('product/<int:id>', gr_shoping.product, name='product'),
    path('address/', gr_shoping.add_model_address, name='add_address_new'),
    path('thank_you/', gr_shoping.thank_you, name='thank_you'),
    path('del/', gr_shoping.del_address, name='del'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += [path('accaunts/', include('django.contrib.auth.urls'))]