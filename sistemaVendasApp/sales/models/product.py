from django.db import models

class Product(models.Model):
  name = models.CharField('Name of the product or service', max_length=100, unique=True)
  comission = models.FloatField('Comission percentage')