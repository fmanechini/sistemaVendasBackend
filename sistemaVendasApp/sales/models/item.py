from django.db import models

class Item(models.Model):
  product = models.ForeignKey('Product', on_delete=models.PROTECT)
  quantity = models.IntegerField('Product quantity')