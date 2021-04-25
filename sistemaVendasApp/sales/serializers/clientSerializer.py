from rest_framework import serializers
from sales.models.client import Client

class ClientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Client
    fields = ('id', 'name')
    read_only_fields = ('id',)