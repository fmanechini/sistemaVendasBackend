import pytest
from sales.models.sale import Sale

@pytest.mark.django_db
def test_sale_model_create(sale):
  assert isinstance(sale, Sale)
