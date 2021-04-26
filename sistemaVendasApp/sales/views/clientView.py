from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.decorators import action
from sales.models.client import Client
from sales.serializers.clientSerializer import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
  serializer_class = ClientSerializer
  queryset = Client.objects.all()

  @action(detail=False, methods=['GET'])
  def get_clients_by_name_like(self, request):
    client_name = self.request.query_params.get('client_name')

    if client_name:
      clients = Client.objects.filter(name__icontains=client_name).order_by('-name')

      serializer = ClientSerializer(clients, many=True)
      return Response(serializer.data)
    else:
      return Response('argumento client_name não pode ser vazio', status=HTTP_400_BAD_REQUEST)