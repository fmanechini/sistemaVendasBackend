import pytest

@pytest.mark.django_db
def test_add_valid_seller(api_client, seller_request):
  response = api_client.post('/sales/seller/', seller_request)
  assert response.status_code == 201

@pytest.mark.django_db
def test_add_duplicated_seller(api_client, seller_request):
  api_client.post('/sales/seller/', seller_request)
  response = api_client.post('/sales/seller/', seller_request)
  assert response.status_code == 400

@pytest.mark.django_db
def test_add_invalid_seller(api_client, empty_seller_request):
  response = api_client.post('/sales/seller/', empty_seller_request)
  assert response.status_code == 400

@pytest.mark.django_db
def test_update_valid_seller(api_client, seller_request, seller2_request):
  response = api_client.post('/sales/seller/', seller_request)
  id_seller = response.json()["id"]
  response2 = api_client.patch(f'/sales/seller/{id_seller}/', seller2_request)
  assert response2.status_code == 200

@pytest.mark.django_db
def test_update_invalid_seller(api_client, seller_request, empty_seller_request):
  response = api_client.post('/sales/seller/', seller_request)
  id_seller = response.json()["id"]
  response2 = api_client.patch(f'/sales/seller/{id_seller}/', empty_seller_request)
  assert response2.status_code == 400

@pytest.mark.django_db
def test_update_seller_not_found(api_client, seller_request, seller2_request):
  response = api_client.post('/sales/seller/', seller_request)
  id_seller = response.json()["id"] + 1
  response2 = api_client.patch(f'/sales/seller/{id_seller}/', seller2_request)
  assert response2.status_code == 404

@pytest.mark.django_db
def test_delete_seller(api_client, seller_request):
  response = api_client.post('/sales/seller/', seller_request)
  id_seller = response.json()["id"]
  response2 = api_client.delete(f'/sales/seller/{id_seller}/')
  assert response2.status_code == 204

@pytest.mark.django_db
def test_delete_seller_not_found(api_client, seller_request):
  response = api_client.post('/sales/seller/', seller_request)
  id_seller = response.json()["id"] + 1
  response2 = api_client.delete(f'/sales/seller/{id_seller}/')
  assert response2.status_code == 404

@pytest.mark.django_db
def test_get_seller_by_name_like(api_client, seller_request):
  api_client.post('/sales/seller/', seller_request)
  response = api_client.get('/sales/seller/get_sellers_by_name_like/?seller_name=f')
  assert response.json()[0]["name"] == "Fernando"