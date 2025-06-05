from django.db import models

# Create your models here.
class Carrera(models.Model):
    id_car = models.AutoField(primary_key=True)
    nombre_car = models.CharField(max_length=100)
    fecha_creacion_car = models.DateField()
    telefono_car = models.CharField(max_length=9, blank=True, null=True)
    
    def __str__(self): # * ESTA FUNCION HACE QUE AL MOMENTO DE IMPRIMIR UN OBJETO DE ESTA CLASE, SE MUESTRE EL NOMBRE DE LA CARRERA
        return self.nombre_car 
    
    