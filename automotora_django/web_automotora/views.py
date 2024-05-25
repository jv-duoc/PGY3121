from django.shortcuts import render
from .models import Auto

# Create your views here.

def inicio(request):

    autos = Auto.objects.filter(comprado = False)

    contexto = {
        "autos":autos
    }

    return render(request,'inicio.html',contexto)

def info(request):
    return render(request,'info.html')