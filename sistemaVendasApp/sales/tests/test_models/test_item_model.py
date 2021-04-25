import pytest
from sales.models.item import Item

@pytest.mark.django_db
def test_item_model_create(item):
  assert isinstance(item, Item)
