from django.shortcuts import render, redirect # * Importa las funciones render y redirect de Django para renderizar plantillas y redirigir a otras vistas
from .models import Carrera # * Importa el modelo Carrera para interactuar con la base de datos
from django.contrib import messages # * Importa el modelo Carrera y el sistema de mensajes de Django para mostrar mensajes al usuario

# Create your views here.
def inicio(request): # * Vista para la página de inicio
    # * Esta vista simplemente renderiza la plantilla index.html
    return render(request, 'index.html')

def carreras(request): # * Vista para mostrar todas las carreras
    
    carrerasDbb = Carrera.objects.all()
    
    print(carrerasDbb)
    
    return render(request, 'carreras.html', {'carreras': carrerasDbb})

def crear_carrera(request): # * Vista para crear una nueva carrera
    if request.method == 'POST':
        nombre = request.POST.get('nombre_car')
        fecha_creacion = request.POST.get('fecha_creacion_car')
        telefono = request.POST.get('telefono_car')
        
        Carrera.objects.create(
            nombre_car=nombre,
            fecha_creacion_car=fecha_creacion,
            telefono_car=telefono
        )
        messages.success(request, '¡Carrera guardada correctamente!') # * Mensaje de éxito al crear la carrera
        return redirect('/carreras')
    
def eliminar_carrera(request, id): # * Vista para eliminar una carrera por su ID
    # * Se busca la carrera por su ID y se elimina
    try:
        carreradb = Carrera.objects.get(id_car=id)
        carreradb.delete()
        messages.success(request, '¡Carrera Borrada de la base de datos correctamente!') # * Mensaje de éxito al eliminar la carrera
        return redirect('/carreras')
    except Carrera.DoesNotExist:
        return render(request, 'error.html', {'message': 'Carrera no encontrada.'})
    
def editar_carrera(request, id): # * Vista para editar una carrera por su ID
    # * Se busca la carrera por su ID y se muestra el formulario de edición
    try:
        carreradb = Carrera.objects.get(id_car=id)
        
        if request.method == 'POST':
            carreradb.nombre_car = request.POST.get('nombre_car')
            carreradb.fecha_creacion_car = request.POST.get('fecha_creacion_car')
            carreradb.telefono_car = request.POST.get('telefono_car')
            carreradb.save()
            messages.success(request, '¡Carrera Actualizada correctamente!') # * Mensaje de éxito al actualizar la carrera
            return redirect('/carreras')
        
        return render(request, 'editar_carrera.html', {'carrera': carreradb})
    
    except Carrera.DoesNotExist:
        return render(request, 'error.html', {'message': 'Carrera no encontrada.'})

def procesar_editar_carrera(request, id): # * Procesa la edición de una carrera
    # * Se busca la carrera por su ID y se actualizan los campos
    if request.method == 'POST':
        nombre = request.POST.get('nombre_car')
        fecha_creacion = request.POST.get('fecha_creacion_car')
        telefono = request.POST.get('telefono_car')
        
        try:
            carreradb = Carrera.objects.get(id_car=id)
            carreradb.nombre_car = nombre
            carreradb.fecha_creacion_car = fecha_creacion
            carreradb.telefono_car = telefono
            carreradb.save()
            messages.success(request, '¡Carrera Actualizada correctamente!') # * Mensaje de éxito al actualizar la carrera
            return redirect('/carreras')
        except Carrera.DoesNotExist:
            return render(request, 'error.html', {'message': 'Carrera no encontrada.'})    
    
      

    
  