from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255,null=False)
    imagen = models.ImageField(upload_to='productos',null=False)
    precio = models.IntegerField(null=False)
