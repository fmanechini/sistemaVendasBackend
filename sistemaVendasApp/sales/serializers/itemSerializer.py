from rest_framework import serializers
from sales.models.item import Item

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = ('id', 'product', 'sale', 'quantity')
    read_only_fields = ('id',)