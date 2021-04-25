import pytest

def test_add_valid_seller():
  assert seller_added == True

def test_add_duplicated_seller():
  assert seller_added == False

def test_add_invalid_seller():
  assert seller_added == False

def test_update_valid_seller():
  assert seller_updated == True

def test_update_invalid_seller():
  assert seller_updated == False

def test_update_seller_not_found():
  assert seller_updated == False

def test_delete_seller():
  assert seller_deleted == True

def test_delete_seller_not_found():
  assert seller_deleted == False