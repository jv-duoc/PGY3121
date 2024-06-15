from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from cryptography.fernet import Fernet
from django.db import transaction
from proyecto.settings import CLAVE_FERNET, SECRET_KEY
from web.models import Compra, DetalleCompra, Producto
from django.contrib import messages
# Create your views here.

def inicio(request):

    productos = Producto.objects.filter(stock__gt=0)

    return render(request,'inicio.html',{"productos":productos});

@login_required(login_url='/login')
def cuenta(request):

    mis_compras = Compra.objects.filter(comprador = request.user)

    f = Fernet(CLAVE_FERNET)
    compras = list(mis_compras.values())
    for compra in compras:
        dir = f.decrypt(compra['direccion'].encode()).decode('utf-8')
        compra['direccion'] = dir

    return render(request,'cuenta.html',{"compras":compras})

@transaction.atomic # Marcamos metodo carro como transacción
@login_required(login_url='/login')
def carro(request):

    f = Fernet(CLAVE_FERNET)

    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        if direccion is None:
            direccion = 'Sin dirección'
        
        lista_ids = request.POST.getlist('productos_id')
        cantidades = request.POST.getlist('productos_cantidad')

        detalles = list(zip(lista_ids,cantidades))
        print(detalles)

        compra = Compra()
        compra.comprador = request.user
        compra.direccion = f.encrypt(direccion.encode('utf-8')).decode('utf-8')
        compra.total = 0
        compra.save()
        dineroTotal = 0


        #detalles!
        try:
            for item in detalles:
                producto = Producto.objects.get(id = item[0])
                cantidad = int(item[1])
                producto.stock -= cantidad

                if producto.stock < 0:
                    raise Exception('No hay suficiente stock para el producto: ' + producto.nombre)
                
                dineroTotal += producto.precio * cantidad
                nuevoDetalle = DetalleCompra()
                nuevoDetalle.producto = producto
                nuevoDetalle.cantidad = cantidad
                nuevoDetalle.compra = compra
                nuevoDetalle.save()
                producto.save()

        except Exception as e:
            transaction.set_rollback(True)
            messages.error(request,str(e))
            return render(request,'carro.html')

        compra.total = dineroTotal
        compra.save()
        return redirect('inicio')


    return render(request,'carro.html')

def salir(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('inicio');

def login_vista(request):

    error = ''

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contra = request.POST.get('password')

        if len(usuario) < 1:
            error += 'Debe ingresar nombre de usuario.'

        if len(contra) < 1:
            error += 'Debe ingresar contraseña.'


        user = authenticate(username = usuario,password = contra)

        if user is None:
            error += 'Las credenciales no son validas.'
        else: 
            login(request,user)
            return redirect('inicio')


    return render(request,'login.html',{"error":error})


def endpoint_productos(request):
    productos = Producto.objects.all()
    lista_productos = list(productos.values())
    return JsonResponse(lista_productos,safe=False)
