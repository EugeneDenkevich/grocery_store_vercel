from django import forms

PRODUCT_QUANTITY_SHOICES = [(i, str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):

    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_SHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)