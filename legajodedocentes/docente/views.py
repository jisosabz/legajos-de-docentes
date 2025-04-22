from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from django.views.decorators.http import require_POST

from .forms import DocenteForm
from .models import Docente

def index(request):
    # para listar todos los docentes o si se ingresa su nombre o su ci para filtrarlos por ello
    query = request.GET.get('search', '')
    docentes = Docente.objects.filter(
        Q(nombre__icontains=query) | Q(ci__icontains=query)
    )
    context = {
        'docentes': docentes
    }
    return render(request, 'docentes/index.html', context)


def view(request,id):
    docente = Docente.objects.get(id=id)
    context = {
        'docente': docente
    }
    return render(request,'docentes/details.html', context)


def edit(request, id):
    docente = Docente.objects.get(id=id)
    # Cuando la página se carga inicialmente para mostrar el formulario de edición con los datos del contacto.
    if request.method == 'GET':
        form = DocenteForm(instance=docente)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'docentes/edit.html', context)
    #  Cuando el usuario envía el formulario con los datos editados para ser guardados en la base de datos.
    elif request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        form.save()
        context = {
            'form': form,
            'id': id,
        }
        messages.success(request,'Docente Actualizado Correctamente')
        return render(request, 'docentes/edit.html', context)
    else:
        return HttpResponse('algo salio mal')

def create(request):
    if request.method == 'GET':
        form = DocenteForm()
        return render(request, 'docentes/create.html', {'form': form})

    elif request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Docente agregado correctamente.')
            return redirect('docente')
        else:
            messages.error(request, 'Hubo un error al agregar el docente. Revisa los campos.')

        return render(request, 'docentes/create.html', {'form': form})

    return HttpResponse('Método no soportado.')

@require_POST
def delete(request, id):
    docente = Docente.objects.get(id=id)
    docente.delete()
    messages.success(request, 'Docente eliminado correctamente.')
    return redirect('docente')


def documento(request):
    return HttpResponse("probando ruta documentos")