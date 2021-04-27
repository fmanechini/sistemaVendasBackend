import pytest

@pytest.mark.django_db
def test_add_valid_product(api_client, product_request):
  response = api_client.post('/sales/product/', product_request)
  assert response.status_code == 201

@pytest.mark.django_db
def test_add_duplicated_product(api_client, product_request):
  api_client.post('/sales/product/', product_request)
  response = api_client.post('/sales/product/', product_request)
  assert response.status_code == 400

@pytest.mark.django_db
def test_add_invalid_product(api_client, empty_product_request):
  response = api_client.post('/sales/product/', empty_product_request)
  assert response.status_code == 400

@pytest.mark.django_db
def test_update_valid_product(api_client, product_request, product_update_request):
  response = api_client.post('/sales/product/', product_request)
  id_product = response.json()["id"]
  response2 = api_client.patch(f'/sales/product/{id_product}/', product_update_request)
  assert response2.status_code == 200

@pytest.mark.django_db
def test_update_invalid_product(api_client, product_request, empty_product_update_request):
  response = api_client.post('/sales/product/', product_request)
  id_product = response.json()["id"]
  response2 = api_client.patch(f'/sales/product/{id_product}/', empty_product_update_request)
  assert response2.status_code == 400

@pytest.mark.django_db
def test_update_product_not_found(api_client, product_request, product_update_request):
  response = api_client.post('/sales/product/', product_request)
  id_product = response.json()["id"] + 1
  response2 = api_client.patch(f'/sales/product/{id_product}/', product_update_request)
  assert response2.status_code == 404

@pytest.mark.django_db
def test_delete_product(api_client, product_request):
  response = api_client.post('/sales/product/', product_request)
  id_product = response.json()["id"]
  response2 = api_client.delete(f'/sales/product/{id_product}/')
  assert response2.status_code == 204

@pytest.mark.django_db
def test_delete_product_not_found(api_client, product_request):
  response = api_client.post('/sales/product/', product_request)
  id_product = response.json()["id"] + 1
  response2 = api_client.delete(f'/sales/product/{id_product}/')
  assert response2.status_code == 404

@pytest.mark.django_db
def test_add_negative_price(api_client, product_request_negative_price):
  response = api_client.post('/sales/product/', product_request_negative_price)
  assert response.status_code == 400

@pytest.mark.django_db
def test_add_negative_comission(api_client, product_request_negative_comission):
  response = api_client.post('/sales/product/', product_request_negative_comission)
  assert response.status_code == 400

@pytest.mark.django_db
def test_add_out_of_bounds_comission(api_client, product_request_out_of_bounds_comission):
  response = api_client.post('/sales/product/', product_request_out_of_bounds_comission)
  assert response.status_code == 400