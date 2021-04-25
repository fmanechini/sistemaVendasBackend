from rest_framework import viewsets
from sales.models.seller import Seller
from sales.serializers.sellerSerializer import SellerSerializer

class SellerViewSet(viewsets.ModelViewSet):
  serializer_class = SellerSerializer
  queryset = Seller.objects.all()