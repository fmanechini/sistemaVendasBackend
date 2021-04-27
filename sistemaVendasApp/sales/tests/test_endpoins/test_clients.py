import pytest

@pytest.mark.django_db
def test_add_valid_client(api_client, client_request):
  response = api_client.post('/sales/clients/', client_request)
  assert response.status_code == 201

@pytest.mark.django_db
def test_add_duplicated_client(api_client, client_request):
  api_client.post('/sales/clients/', client_request)
  response = api_client.post('/sales/clients/', client_request)
  assert response.status_code == 400

@pytest.mark.django_db
def test_add_invalid_client(api_client, empty_client_request):
  response = api_client.post('/sales/clients/', empty_client_request)
  assert response.status_code == 400

@pytest.mark.django_db
def test_update_valid_client(api_client, client_request, client2_request):
  response = api_client.post('/sales/clients/', client_request)
  id_client = response.json()["id"]
  response2 = api_client.patch(f'/sales/clients/{id_client}/', client2_request)
  assert response2.status_code == 200

@pytest.mark.django_db
def test_update_invalid_client(api_client, client_request, empty_client_request):
  response = api_client.post('/sales/clients/', client_request)
  id_client = response.json()["id"]
  response2 = api_client.patch(f'/sales/clients/{id_client}/', empty_client_request)
  assert response2.status_code == 400

@pytest.mark.django_db
def test_update_client_not_found(api_client, client_request, client2_request):
  response = api_client.post('/sales/clients/', client_request)
  id_client = response.json()["id"] + 1
  response2 = api_client.patch(f'/sales/clients/{id_client}/', client2_request)
  assert response2.status_code == 404

@pytest.mark.django_db
def test_delete_client(api_client, client_request):
  response = api_client.post('/sales/clients/', client_request)
  id_client = response.json()["id"]
  response2 = api_client.delete(f'/sales/clients/{id_client}/')
  assert response2.status_code == 204

@pytest.mark.django_db
def test_delete_client_not_found(api_client, client_request):
  response = api_client.post('/sales/clients/', client_request)
  id_client = response.json()["id"] + 1
  response2 = api_client.delete(f'/sales/clients/{id_client}/')
  assert response2.status_code == 404

@pytest.mark.django_db
def test_get_client_by_name_like(api_client, client_request):
  api_client.post('/sales/clients/', client_request)
  response = api_client.get('/sales/clients/get_clients_by_name_like/?client_name=g')
  assert response.json()[0]["name"] == "Geraldo"