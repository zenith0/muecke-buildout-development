__author__ = 'stefan'
from django import forms

from models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product

    # validate the price
    def clean_price(self):
        # check the value of price
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be greater than zero')
        return self.cleaned_data['price']