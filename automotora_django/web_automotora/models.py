import datetime
import uuid
from django.db import models

# Create your models here.

class Auto(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    marca = models.CharField(max_length=255,null=False)
    modelo = models.CharField(max_length=255,null=False)
    año = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    fecha = models.DateTimeField(null=False,default=datetime.date.today(),editable=False)
    comprado = models.BooleanField(null=False, default= False)
    imagen = models.ImageField(upload_to='static/subidas',null=True)

    def __str__(self):
        return str(self.año)+' '+self.marca+' '+self.modelo

class Tipo(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length=255, null = False)

    def __str__(self):
        return self.nombre