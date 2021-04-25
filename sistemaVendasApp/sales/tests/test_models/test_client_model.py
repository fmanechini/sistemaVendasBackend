import pytest
from sales.models.client import Client

@pytest.mark.django_db
def test_client_model_create(client):
  assert isinstance(client, Client)
