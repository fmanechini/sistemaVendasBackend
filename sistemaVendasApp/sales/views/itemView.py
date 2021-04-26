from rest_framework import viewsets
from sales.models.item import Item
from sales.serializers.itemSerializer import ItemSerializer, ItemPostSerializer

class ItemViewSet(viewsets.ModelViewSet):
  serializer_class = ItemSerializer
  queryset = Item.objects.all()

  # def create(self, request):
  #   serializer = ItemPostSerializer(data=request.data)
  #   if serializer.is_valid():
  #     serializer.save()
  def get_serializer_class(self):
    if self.action in ['retrieve', 'list']:
        return ItemSerializer
    else:
        return ItemPostSerializer