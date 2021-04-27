from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from rest_framework.decorators import action
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
  
  @action(detail=False, methods=['GET'])
  def get_comission_in_time_range(self, request):
    """
    returns total comission from a specific seller between a time range
    """
    seller_id = self.request.query_params.get('seller_id')
    start_date = self.request.query_params.get('start_date')
    end_date = self.request.query_params.get('end_date')
    if seller_id and start_date and end_date:
      sales = Sale.objects.filter(seller__id=seller_id, sale_datetime__range=[start_date, end_date])
      sales_serialized = SaleSerializer(sales, many=True)
      total_comission = 0
      for sale in sales_serialized.data:
        for item in sale['items']:
          total_comission += item['product']['price'] * float(item['quantity']) * item['applied_comission']

      return Response(total_comission, status=HTTP_200_OK)
    return Response(
      'arguments seller_id, start_date and end_date must not be null', 
      status=status.HTTP_400_BAD_REQUEST
      )