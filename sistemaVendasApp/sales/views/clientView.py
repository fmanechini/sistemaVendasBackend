from rest_framework import viewsets
from sales.models.client import Client
from sales.serializers.clientSerializer import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
  serializer_class = ClientSerializer
  queryset = Client.objects.all()