from itertools import product
from urllib.request import ProxyDigestAuthHandler
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
