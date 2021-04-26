from django.db import models
from sales.models.validators import validate_comissions

class Item(models.Model):
  product = models.ForeignKey('Product', on_delete=models.PROTECT)
  quantity = models.IntegerField('Product quantity')
  applied_comission = models.FloatField('Comission percentage applied for certain sale', 
                      validators=[validate_comissions])
  sale = models.ForeignKey('Sale', on_delete=models.CASCADE, related_name='items')