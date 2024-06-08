from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarea(models.Model):
    id = models.BigAutoField(primary_key=True)
    texto = models.CharField(null = False,max_length=1024)
    completado = models.BooleanField()
    creador = models.ForeignKey(User,null=True,on_delete=models.CASCADE)