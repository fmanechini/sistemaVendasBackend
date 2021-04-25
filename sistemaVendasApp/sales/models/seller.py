from django.db import models

class Seller(models.Model):
  name = models.CharField('Name of the seller', max_length=100, unique=True)