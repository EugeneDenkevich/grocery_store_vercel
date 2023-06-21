from pickle import FALSE
from django.db import models
from django.contrib.auth.models import User


class Delivery(models.Model):

    METHODS = [('p', 'Pick up in the pick-up point'),
               ('d', 'Deliver to my appartment')]

    country = models.CharField(blank=False, max_length=100)
    city = models.CharField(blank=False, max_length=100)
    address = models.CharField(blank=False, max_length=200)
    phone = models.CharField(blank=False, max_length=100)
    comment = models.TextField(max_length=300)
    method = models.CharField(choices=METHODS, max_length=1, blank=False)

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

CATEGORY = [('Fruits', 'Fruits'), ('Vegetables', 'Vegitables'), ('Milk-and-meat', 'Milk and Meat')]

class Cart(models.Model):

    product = models.CharField(blank=False, max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

class Product(models.Model):

    name = models.CharField(blank=False, max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    company = models.CharField(blank=False, max_length=100)
    image = models.ImageField(upload_to='uploads')

    category = models.CharField(choices=CATEGORY, max_length=20, blank=False)