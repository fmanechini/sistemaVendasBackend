from rest_framework import serializers
from sales.models.seller import Seller

class SellerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Seller
    fields = ('id', 'name')
    read_only_fields = ('id',)