import code
from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=500)

class Offer(models.Model):
    code = models.CharField(max_length=16)
    description = models.CharField(max_length=250)
    discount = models.FloatField()

