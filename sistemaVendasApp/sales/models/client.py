from django.db import models

class Client(models.Model):
  name = models.CharField('Client name', max_length=100, unique=True)
