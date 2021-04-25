import pytest

def test_add_valid_sale():
  assert sale_added == True

def test_add_sale_with_higher_percentage():
  for product in sales.products:
    assert product.comission <= 0.05

def test_add_sale_with_lower_percentage():
  for product in sales.products:
    assert product.comission >= 0.04

def test_add_invalid_sale():
  assert sale_added == False

def test_delete_sale():
  assert sale_deleted == True

def test_delete_sale_not_found():
  assert sale_deleted == False