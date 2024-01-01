# forms.py
from django import forms
from .models import Product


class AddProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    gram = forms.DecimalField()
    quantity = forms.IntegerField()
    discount = forms.DecimalField(required=False)
