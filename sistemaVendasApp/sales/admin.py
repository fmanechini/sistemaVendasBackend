from django.contrib import admin
from sales.models.client import Client
from sales.models.item import Item
from sales.models.product import Product
from sales.models.sale import Sale
from sales.models.seller import Seller

admin.site.register(Client)
admin.site.register(Item)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Seller)
