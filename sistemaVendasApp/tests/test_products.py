import pytest

def test_add_valid_product():
  assert product_added == True

def test_add_duplicated_product():
  assert product_added == False

def test_add_invalid_product():
  assert product_added == False

def test_update_valid_product():
  assert product_updated == True

def test_update_invalid_product():
  assert product_updated == False

def test_update_product_not_found():
  assert product_updated == False

def test_delete_product():
  assert product_deleted == True

def test_delete_product_not_found():
  assert product_deleted == False