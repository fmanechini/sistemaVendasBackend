from django.db import models

class Client(models.Model):
  name = models.CharField('Nome do Cliente', max_length=100, unique=True)
