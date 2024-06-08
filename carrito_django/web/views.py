from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    return render(request,'inicio.html');

@login_required(login_url='/login')
def cuenta(request):
    return render(request,'cuenta.html')


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