from rest_framework import viewsets
from sales.models.sale import Sale
from sales.models.item import Item
from sales.serializers.saleSerializer import SaleSerializer, SalePostSerializer

class SaleViewSet(viewsets.ModelViewSet):
  serializer_class = SaleSerializer
  queryset = Sale.objects.all()

  def get_serializer_class(self):
    if self.action in ['retrieve', 'list']:
        return SaleSerializer
    else:
        return SalePostSerializer

  def post(self, request, *args, **kwargs):
    serializer = SalePostSerializer(data=request.data)
    if serializer.is_valid():
        sale = serializer.save()
        serializer = SalePostSerializer(sale)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)