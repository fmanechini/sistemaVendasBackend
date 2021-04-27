from rest_framework import serializers
from sales.serializers.clientSerializer import ClientSerializer
from sales.serializers.sellerSerializer import SellerSerializer
from sales.serializers.itemSerializer import ItemSerializer, ItemPostSerializer
from sales.serializers.productSerializer import ProductSerializer
from sales.models.sale import Sale
from sales.models.client import Client
from sales.models.seller import Seller
from sales.models.item import Item
import datetime

class SaleSerializer(serializers.ModelSerializer):
  client = ClientSerializer()
  seller = SellerSerializer()
  items = ItemSerializer(many=True)

  class Meta:
    model = Sale
    fields = ('id', 'sale_datetime', 'client', 'seller', 'items')
    read_only_fields = ('id',)

class SalePostSerializer(serializers.ModelSerializer):
  client = serializers.SlugRelatedField(
    slug_field='name',
    queryset=Client.objects.all()
  )

  seller = serializers.SlugRelatedField(
    slug_field='name',
    queryset=Seller.objects.all()
  )

  items = ItemPostSerializer(many=True)

  def create(self, validated_data):
    items_data = validated_data.pop('items')
    sale = Sale.objects.create(**validated_data)
    items_serializer = ItemPostSerializer(many=True)

    #validate conditions for comissions
    sale_datetime = validated_data.get('sale_datetime').time()
    lower_time = datetime.time(hour=0,minute=0,second=0)
    higher_time = datetime.time(hour=12,minute=0,second=0)
    for item in items_data:
      product = ProductSerializer(item['product'])
      product = product.data
      if sale_datetime >= lower_time and sale_datetime <= higher_time:
        if product['comission'] >= 0.05:
          item['applied_comission'] = 0.05
        else:
          item['applied_comission'] = product['comission']
      else:
        if product['comission'] <= 0.04:
          item['applied_comission'] = 0.04
        else:
          item['applied_comission'] = product['comission']
      item['sale'] = sale
    items = items_serializer.create(items_data)
    return sale

  class Meta:
    model = Sale
    fields = ('id', 'client', 'seller', 'sale_datetime', 'items')
    read_only_fields = ('id',)
