from django.db import models
from sales.models.validators import validate_comissions, greater_than_zero

class Product(models.Model):
  name = models.CharField('Name of the product or service', max_length=100, unique=True)
  comission = models.FloatField('Comission percentage', validators=[validate_comissions])
  price = models.FloatField('Price from product or service', default=0.0, validators=[greater_than_zero])