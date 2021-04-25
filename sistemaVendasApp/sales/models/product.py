from django.db import models

class Product(models.Model):
  name = models.CharField('Name of the product or service', max_length=100, unique=True)
  comission = models.FloatField('Comission percentage')
  price = models.DecimalField('Price from product or service', default=0.0, max_digits=5, decimal_places=2)