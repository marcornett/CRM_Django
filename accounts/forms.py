from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        # Grabs all the variables from the assigned Model
        # In this case: customer, product, date_created, status
        # Can also: fields = ['customer', 'product', 'date_created', 'status']
        fields = '__all__'
        