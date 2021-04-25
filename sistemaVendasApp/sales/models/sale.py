from django.db import models

class Sale(models.Model):
  sale_datetime = models.DateTimeField('Date and time of the sale')
  client = models.ForeignKey('Client', on_delete=models.PROTECT)
  seller = models.ForeignKey('Seller', on_delete=models.PROTECT)
