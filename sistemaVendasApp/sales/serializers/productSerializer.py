from rest_framework import serializers
from sales.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ('id', 'name', 'comission', 'price')
    read_only_fields = ('id',)