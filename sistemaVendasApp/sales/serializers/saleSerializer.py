from rest_framework import serializers
from sales.models.sale import Sale

class SaleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sale
    fields = ('id', 'sale_datetime', 'client', 'seller')
    read_only_fields = ('id',)