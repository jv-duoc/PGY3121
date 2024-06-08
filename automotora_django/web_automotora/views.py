from django.shortcuts import render
from .models import Auto,Tipo
import datetime
from django.db import connection

# Create your views here.

def inicio(request):
    
    datos = ejecutar_sql('SELECT COUNT(*) as autos_totales FROM web_automotora_auto WHERE comprado=0')

    tipos = Tipo.objects.all()

    autos = Auto.objects.filter(comprado = False)

    tipo_filtrado = request.GET.get('tipo')
    precio_max = request.GET.get('precio_max')
    año = request.GET.get('año')

    if año:
        autos = autos.filter(año = año)

    if precio_max:
        autos = autos.filter(precio__lte = precio_max)

    if tipo_filtrado:
        tipo = Tipo.objects.get(nombre = tipo_filtrado)
        autos = autos.filter(tipo = tipo)

    contexto = {
        "autos":autos,
        "datos":datos[0],
        "tipos":tipos,
        "precio_max":precio_max
    }

    return render(request,'inicio.html',contexto)

def info(request):
    hora_actual = datetime.datetime.now()
    bolsa = {
        "hora":hora_actual,
        "version":"2.0"
    }
    return render(request,'info.html',bolsa)

def listar_tipos(request):

    tipos_detalle = ejecutar_sql('SELECT t.nombre as nombre,COUNT(*) as stock FROM web_automotora_auto a JOIN web_automotora_tipo t ON a.tipo_id = t.id GROUP BY t.id,t.nombre')

    #tipos = Tipo.objects.all()

    bolsa = {
        #"tipos":tipos,
        "tipos":tipos_detalle
    }

    return render(request,'tipos.html',bolsa)


def ejecutar_sql(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultado = dictfetchall(cursor)

    return resultado

def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]