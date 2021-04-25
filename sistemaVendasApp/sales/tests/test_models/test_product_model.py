import pytest
from sales.models.product import Product

@pytest.mark.django_db
def test_product_model_create(product):
  assert isinstance(product, Product)
