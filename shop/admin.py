# registering the model is imp to display it in the django-admin panel

from django.contrib import admin

# importing product class from shop/models
from .models import Product
from .models import Feedback
from .models import Order,OrderUpdate

# Register your models here.
admin.site.register(Product)
admin.site.register(Feedback)
admin.site.register(Order)
admin.site.register(OrderUpdate)