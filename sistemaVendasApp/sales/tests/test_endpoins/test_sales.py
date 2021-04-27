import pytest

@pytest.mark.django_db
def test_add_valid_sale(
  api_client, 
  client_request,  
  seller_request, 
  product_request, 
  product2_request,
  sale_request):

  api_client.post('/sales/clients/', client_request)
  api_client.post('/sales/seller/', seller_request)
  api_client.post('/sales/product/', product_request)
  api_client.post('/sales/product/', product2_request)
  response = api_client.post('/sales/sale/', sale_request, format='json')
  #comission between 00:00 and 12:00 must be max 0.05
  assert response.json()['items'][1]['applied_comission'] == 0.05
  assert response.status_code == 201

@pytest.mark.django_db
def test_add_valid_sale_after_12(
  api_client, 
  client_request,  
  seller_request, 
  product_request, 
  product2_request,
  sale_request_after_12):

  api_client.post('/sales/clients/', client_request)
  api_client.post('/sales/seller/', seller_request)
  api_client.post('/sales/product/', product_request)
  api_client.post('/sales/product/', product2_request)
  response = api_client.post('/sales/sale/', sale_request_after_12, format='json')
  #comission between 00:00 and 12:00 must be min 0.04
  assert response.json()['items'][0]['applied_comission'] == 0.04
  assert response.status_code == 201

@pytest.mark.django_db
def test_add_invalid_sale(api_client, invalid_sale_request):
  response = api_client.post('/sales/sale/', invalid_sale_request)
  assert response.status_code == 400

@pytest.mark.django_db
def test_delete_sale(
  api_client,
  client_request,  
  seller_request, 
  product_request, 
  product2_request,
  sale_request):
  api_client.post('/sales/clients/', client_request)
  api_client.post('/sales/seller/', seller_request)
  api_client.post('/sales/product/', product_request)
  api_client.post('/sales/product/', product2_request)
  response = api_client.post('/sales/sale/', sale_request, format='json')
  id_sale = response.json()["id"]
  response2 = api_client.delete(f'/sales/sale/{id_sale}/')
  assert response2.status_code == 204

@pytest.mark.django_db
def test_delete_invalid_sale(
  api_client,
  client_request,  
  seller_request, 
  product_request, 
  product2_request,
  sale_request):
  api_client.post('/sales/clients/', client_request)
  api_client.post('/sales/seller/', seller_request)
  api_client.post('/sales/product/', product_request)
  api_client.post('/sales/product/', product2_request)
  response = api_client.post('/sales/sale/', sale_request, format='json')
  id_sale = response.json()["id"] + 1
  response2 = api_client.delete(f'/sales/sale/{id_sale}/')
  assert response2.status_code == 404

@pytest.mark.django_db
def test_add_negative_quantity(
  api_client, 
  client_request,  
  seller_request, 
  product_request, 
  product2_request,
  negative_quantity_sale_request):

  api_client.post('/sales/clients/', client_request)
  api_client.post('/sales/seller/', seller_request)
  api_client.post('/sales/product/', product_request)
  api_client.post('/sales/product/', product2_request)
  response = api_client.post('/sales/sale/', negative_quantity_sale_request, format='json')
  assert response.status_code == 400

@pytest.mark.django_db
def test_add_zero_quantity(
  api_client, 
  client_request,  
  seller_request, 
  product_request, 
  product2_request,
  zero_quantity_sale_request):

  api_client.post('/sales/clients/', client_request)
  api_client.post('/sales/seller/', seller_request)
  api_client.post('/sales/product/', product_request)
  api_client.post('/sales/product/', product2_request)
  response = api_client.post('/sales/sale/', zero_quantity_sale_request, format='json')
  assert response.status_code == 400

@pytest.mark.django_db
def test_get_comission_in_time_range(
  api_client, 
  client_request,  
  seller_request, 
  product_request, 
  product2_request,
  sale_request,
  sale_request_after_12):

  api_client.post('/sales/clients/', client_request)
  resp = api_client.post('/sales/seller/', seller_request)
  api_client.post('/sales/product/', product_request)
  api_client.post('/sales/product/', product2_request)
  api_client.post('/sales/sale/', sale_request, format='json')
  api_client.post('/sales/sale/', sale_request_after_12, format='json')
  seller_id = resp.json()['id']
  response = api_client.get(
    f'/sales/sale/get_comission_in_time_range/?seller_id={seller_id}&start_date=2020-02-21&end_date=2022-02-18'
    )
  assert response.json() == 3.25