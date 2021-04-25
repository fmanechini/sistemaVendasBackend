from rest_framework import viewsets
from sales.models.item import Item
from sales.serializers.itemSerializer import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
  serializer_class = ItemSerializer
  queryset = Item.objects.all()