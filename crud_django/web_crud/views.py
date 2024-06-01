from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from web_crud.forms import NuevaTareaForm
from .models import Tarea
# Create your views here.

def lista(request):

    todas_tareas = Tarea.objects.all()

    context = {
        "tareas":todas_tareas
    }

    return render(request,'lista.html',context)

def borrar(request,id):
    return render(request,'borrar.html',{"id":id})

def nueva(request):

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

            nueva_tarea.save()
            return HttpResponseRedirect('/')

    else:
        formulario = NuevaTareaForm()

    return render(request,'nueva.html',{"form":formulario,"metodo":metodo})