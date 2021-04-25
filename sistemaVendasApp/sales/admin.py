from django.contrib import admin
from .models.client import Client
from .models.item import Item
from .models.product import Product
from .models.sale import Sale
from .models.seller import Seller

admin.site.register(Client)
admin.site.register(Item)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Seller)
