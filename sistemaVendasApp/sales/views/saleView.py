from rest_framework import viewsets
from sales.models.sale import Sale
from sales.serializers.saleSerializer import SaleSerializer

class SaleViewSet(viewsets.ModelViewSet):
  serializer_class = SaleSerializer
  queryset = Sale.objects.all()