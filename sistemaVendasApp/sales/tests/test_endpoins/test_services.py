import pytest

def test_add_valid_service():
  assert service_added == True

def test_add_duplicated_service():
  assert service_added == False

def test_add_invalid_service():
  assert service_added == False

def test_update_valid_service():
  assert service_updated == True

def test_update_invalid_service():
  assert service_updated == False

def test_update_service_not_found():
  assert service_updated == False

def test_delete_service():
  assert service_deleted == True

def test_delete_service_not_found():
  assert service_deleted == False