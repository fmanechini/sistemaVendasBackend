from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.decorators import action
from sales.models.seller import Seller
from sales.serializers.sellerSerializer import SellerSerializer

class SellerViewSet(viewsets.ModelViewSet):
  serializer_class = SellerSerializer
  queryset = Seller.objects.all()

  @action(detail=False, methods=['GET'])
  def get_sellers_by_name_like(self, request):
    seller_name = self.request.query_params.get('seller_name')

    if seller_name:
      sellers = Seller.objects.filter(name__icontains=seller_name).order_by('-name')

      serializer = SellerSerializer(sellers, many=True)
      return Response(serializer.data)
    else:
      return Response('argumento seller_name não pode ser vazio', status=HTTP_400_BAD_REQUEST)