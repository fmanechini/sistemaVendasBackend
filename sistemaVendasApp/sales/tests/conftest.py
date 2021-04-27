import pytest
from rest_framework.test import APIClient
from datetime import datetime
from sales.models.product import Product
from sales.models.client import Client
from sales.models.item import Item
from sales.models.seller import Seller
from sales.models.sale import Sale

#### model fixtures ####

@pytest.fixture
@pytest.mark.django_db
def product():
  product = Product.objects.create(
    name="lápis",
    comission=0.03,
    price=1.59)
  return product

@pytest.fixture
@pytest.mark.django_db
def client():
  client = Client.objects.create(name="geraldo")
  return client

@pytest.fixture
@pytest.mark.django_db
def seller():
  seller = Seller.objects.create(name="Alberto")
  return seller

@pytest.fixture
@pytest.mark.django_db
def item(product, sale):
  item = Item.objects.create(
    product=product,
    sale=sale,
    quantity=4,
    applied_comission=0.05
  )
  return item

@pytest.fixture
@pytest.mark.django_db
def secondItem(product, sale):
  secondItem = Item.objects.create(
    product=product,
    sale=sale,
    quantity=2
  )
  return secondItem

@pytest.fixture
@pytest.mark.django_db
def sale(client, seller):
  sale = Sale.objects.create(
    sale_datetime = datetime.now(),
    client = client,
    seller = seller,
  )
  return sale

#### API FIXTURES ####

@pytest.fixture
def api_client():
  return APIClient()

#### client requests #### 

@pytest.fixture
def client_request():
  return {"name": "Geraldo"}

@pytest.fixture
def client2_request():
  return {"name": "Alfredo"}

@pytest.fixture
def empty_client_request():
  return {"name": ""}

#### seller requests #### 

@pytest.fixture
def seller_request():
  return {"name": "Fernando"}

@pytest.fixture
def seller2_request():
  return {"name": "Alfredo"}

@pytest.fixture
def empty_seller_request():
  return {"name": ""}

#### products requests #### 

@pytest.fixture
def product_request():
  return {"name": "lapis", "price": 5, "comission": 0.03}

@pytest.fixture
def product_request_negative_price():
  return {"name": "lapis", "price": -5, "comission": 0.03}

@pytest.fixture
def product_request_negative_comission():
  return {"name": "lapis", "price": 5, "comission": -0.03}

@pytest.fixture
def product_request_out_of_bounds_comission():
  return {"name": "lapis", "price": 5, "comission": 0.13}

@pytest.fixture
def product2_request():
  return {"name": "caneta", "price": 5, "comission": 0.08}

@pytest.fixture
def product_update_request():
  return {"name": "caneta"}

@pytest.fixture
def empty_product_update_request():
  return {"name": ""}

@pytest.fixture
def empty_product_request():
  return {"name": "", "price": 5, "comission": 0.03}

#### sale request ####

@pytest.fixture
def sale_request():
  return {
    "sale_datetime": "2020-06-12 09:55:22",
    "client": "Geraldo",
    "seller": "Fernando",
    "items": [
    {
        "product": "lapis",
        "quantity": 5
    },
    {
        "product": "caneta",
        "quantity": 10
    }]
}

@pytest.fixture
def sale_request_after_12():
  return {
    "sale_datetime": "1990-06-12 12:55:22",
    "client": "Geraldo",
    "seller": "Fernando",
    "items": [
    {
        "product": "lapis",
        "quantity": 5
    },
    {
        "product": "caneta",
        "quantity": 10
    }]
}

@pytest.fixture
def negative_quantity_sale_request():
  return {
    "sale_datetime": "2020-06-12 09:55:22",
    "client": "Geraldo",
    "seller": "Fernando",
    "items": [
    {
        "product": "lapis",
        "quantity": -5
    },
    {
        "product": "caneta",
        "quantity": 10
    }]
}

@pytest.fixture
def zero_quantity_sale_request():
  return {
    "sale_datetime": "2020-06-12 09:55:22",
    "client": "Geraldo",
    "seller": "Fernando",
    "items": [
    {
        "product": "lapis",
        "quantity": 5
    },
    {
        "product": "caneta",
        "quantity": 0
    }]
}

@pytest.fixture
def invalid_sale_request():
  return {
    "sale_datetime": "2020-06-12 09:55:22",
    "client": "",
    "seller": "Fernando",
    "items": [
    {
        "product": "lapis",
        "quantity": 5
    },
    {
        "product": "caneta",
        "quantity": 10
    }]
}