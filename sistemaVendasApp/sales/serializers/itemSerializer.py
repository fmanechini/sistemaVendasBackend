from rest_framework import serializers
from sales.serializers.productSerializer import ProductSerializer
from sales.models.item import Item
from sales.models.product import Product
from sales.models.sale import Sale

class ItemSerializer(serializers.ModelSerializer):
  product = ProductSerializer()

  class Meta:
    model = Item
    fields = ('id', 'product', 'quantity', 'applied_comission')
    read_only_fields = ('id',)

class ItemPostSerializer(serializers.ModelSerializer):
  product = serializers.SlugRelatedField(
    slug_field='name',
    queryset=Product.objects.all()
  )

  class Meta:
    model = Item
    fields = ('id', 'product', 'quantity', 'applied_comission')
    read_only_fields = ('id',)