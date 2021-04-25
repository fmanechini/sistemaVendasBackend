import pytest
from sales.models.seller import Seller

@pytest.mark.django_db
def test_seller_model_create(seller):
  assert isinstance(seller, Seller)
