from django.contrib import admin

# Register your models here.
from .models import *

# register Customer model to database
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
