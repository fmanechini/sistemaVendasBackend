from django.db import models

class Item(models.Model):
  product = models.ForeignKey('Product', on_delete=models.PROTECT)
  sale = models.ForeignKey('Sale', on_delete=models.CASCADE)
  quantity = models.IntegerField('Product quantity')