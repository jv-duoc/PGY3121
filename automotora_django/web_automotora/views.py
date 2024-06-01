from django.shortcuts import render
from .models import Auto,Tipo
import datetime

# Create your views here.

def inicio(request):

    autos = Auto.objects.filter(comprado = False)

    contexto = {
        "autos":autos
    }

    return render(request,'inicio.html',contexto)

def info(request):
    hora_actual = datetime.datetime.now()
    bolsa = {
        "hora":hora_actual,
        "version":"1.0"
    }
    return render(request,'info.html',bolsa)

def listar_tipos(request):

    tipos = Tipo.objects.all()

    bolsa = {
        "tipos":tipos
    }

    return render(request,'tipos.html',bolsa)