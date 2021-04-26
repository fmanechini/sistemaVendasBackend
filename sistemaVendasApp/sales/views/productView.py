from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.decorators import action
from sales.models.product import Product
from sales.serializers.productSerializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()

  @action(detail=False, methods=['GET'])
  def get_products_by_name_like(self, request):
    product_name = self.request.query_params.get('product_name')

    if product_name:
      products = Product.objects.filter(name__icontains=product_name).order_by('-name')

      serializer = ProductSerializer(products, many=True)
      return Response(serializer.data)
    else:
      return Response('argumento product_name não pode ser vazio', status=HTTP_400_BAD_REQUEST)