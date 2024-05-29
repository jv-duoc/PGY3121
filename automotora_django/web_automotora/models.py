from django.db import models

# Create your models here.

class Auto(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    marca = models.CharField(max_length=255,null=False)
    modelo = models.CharField(max_length=255,null=False)
    año = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)