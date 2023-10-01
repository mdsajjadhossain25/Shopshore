from django import forms
from .models import Order

# code goes here


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'address_line_1',
                  'address_line_2', 'country', 'state', 'city', 'order_note']
