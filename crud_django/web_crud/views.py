from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from web_crud.forms import NuevaTareaForm, RegistroForm
from django.contrib import messages

from .models import Tarea
# Create your views here.

@login_required(login_url='/login')
def salir(request):
    logout(request)
    return redirect('lista')

def lista(request):

    todas_tareas = Tarea.objects.all()

    context = {
        "tareas":todas_tareas
    }

    return render(request,'lista.html',context)

def borrar(request,id):

    if request.method == 'POST':
        tarea = Tarea.objects.get(id = id)
        tarea.delete()
        return redirect('lista')

    return render(request,'borrar.html',{"id":id})

def editar(request,id):
    tarea = Tarea.objects.get(id = id)

    if request.method == 'POST':
        form = NuevaTareaForm(request.POST)
        if form.is_valid():
            texto = form.cleaned_data.get('texto')
            completado = form.cleaned_data.get('completado')
            tarea.texto = texto
            tarea.completado = completado
            tarea.save()
            return redirect('lista')
    else:
        form = NuevaTareaForm(initial={
                "texto":tarea.texto,
                "completado":tarea.completado
            })

    return render(request,'editar.html',{"tarea":tarea,"form":form})

#@login_required(login_url='/login')
def nueva(request):

    if not request.user.is_authenticated:
        return redirect('login')

    metodo = request.method

    if request.method == 'POST':
        #hacer cosas
        formulario = NuevaTareaForm(request.POST)

        if formulario.is_valid():
            texto_del_form = formulario.cleaned_data['texto']
            #prodriamos validar mas cosas de texto
            completado_del_form = formulario.cleaned_data['completado']
            print(completado_del_form)
            #nueva_tarea = Tarea(texto = texto_del_form,completado = completado_del_form)
            nueva_tarea = Tarea()
            nueva_tarea.texto = texto_del_form
            nueva_tarea.completado = completado_del_form
            nueva_tarea.creador = request.user

            nueva_tarea.save()
            return redirect('lista')

    else:
        formulario = NuevaTareaForm()

    return render(request,'nueva.html',{"form":formulario,"metodo":metodo})


def view_login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')

        if(len(usuario) < 1):
            messages.error(request,'Debe ingresar un nombre de usuario')

        if(len(password) < 1):
            messages.error(request,'Debe ingresar la contraseña')

        usuario = authenticate(username=usuario,password = password)
        if usuario is None:
            messages.error(request,'Usuario o contraseña incorrecto')
        else:
            login(request,usuario)
            return redirect('lista')



    return render(request,'login.html')

def view_registro(request):
    form = RegistroForm()

    if request.method == 'POST':
        form = RegistroForm(request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('usuario')
            pass1 = form.cleaned_data.get('password')
            pass2 = form.cleaned_data.get('password2')

            if pass1 == pass2:
                
                if User.objects.filter(username = usuario).all().exists():
                    messages.error(request,'El usuario ya esta registrado!')
                else:
                    user = User.objects.create_user(username = usuario, email= usuario,password = pass1)
                    user.save()
                    return redirect('login')

            else:
                messages.error(request,'Las contraseñas deben coincidir')


    else:
        form = RegistroForm()

    return render(request,'registro.html',{"form":form})