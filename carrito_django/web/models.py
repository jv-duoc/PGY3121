from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255,null=False)
    precio = models.IntegerField(null=False)
    stock = models.IntegerField(null=False,default=10)

    def __str__(self):
        return self.nombre
    
class Compra(models.Model):
    id = models.BigAutoField(primary_key=True)
    total = models.IntegerField(null=False)
    fecha = models.DateTimeField(auto_now_add=True)
    direccion = models.CharField(max_length=2048,null=False)
    comprador = models.ForeignKey(User,on_delete=models.CASCADE)

class DetalleCompra(models.Model):
    id = models.BigAutoField(primary_key=True)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)
    compra = models.ForeignKey(Compra,on_delete=models.CASCADE)