from django.shortcuts import render, redirect
from .models import Carrera

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def carreras(request):
    
    carrerasDbb = Carrera.objects.all()
    
    print(carrerasDbb)
    
    return render(request, 'carreras.html', {'carreras': carrerasDbb})

def crear_carrera(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_car')
        fecha_creacion = request.POST.get('fecha_creacion_car')
        telefono = request.POST.get('telefono_car')
        
        Carrera.objects.create(
            nombre_car=nombre,
            fecha_creacion_car=fecha_creacion,
            telefono_car=telefono
        )
        
        return redirect('/carreras')
    
def eliminar_carrera(request, id):
    try:
        carreradb = Carrera.objects.get(id_car=id)
        carreradb.delete()
        return redirect('/carreras')
    except Carrera.DoesNotExist:
        return render(request, 'error.html', {'message': 'Carrera no encontrada.'})
    
def editar_carrera(request, id):
    try:
        carreradb = Carrera.objects.get(id_car=id)
        
        if request.method == 'POST':
            carreradb.nombre_car = request.POST.get('nombre_car')
            carreradb.fecha_creacion_car = request.POST.get('fecha_creacion_car')
            carreradb.telefono_car = request.POST.get('telefono_car')
            carreradb.save()
            return redirect('/carreras')
        
        return render(request, 'editar_carrera.html', {'carrera': carreradb})
    
    except Carrera.DoesNotExist:
        return render(request, 'error.html', {'message': 'Carrera no encontrada.'})
        
        
    
  