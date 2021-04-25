import pytest
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
    quantity=4
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
