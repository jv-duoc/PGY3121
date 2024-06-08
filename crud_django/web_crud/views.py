from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

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
            return redirect('lista')

    else:
        formulario = NuevaTareaForm()

    return render(request,'nueva.html',{"form":formulario,"metodo":metodo})