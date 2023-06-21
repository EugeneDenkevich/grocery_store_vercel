from django import forms
from .models import Delivery

class AddAddressViaModelForm(forms.ModelForm):

    class Meta():

        model = Delivery
        fields = ('country', 'city', 'address', 'phone', 'comment', 'method')