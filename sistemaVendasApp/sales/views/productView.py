from rest_framework import viewsets
from sales.models.product import Product
from sales.serializers.productSerializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()