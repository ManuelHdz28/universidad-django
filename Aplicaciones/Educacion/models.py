from django.db import models

# Create your models here.
class Carrera(models.Model):
    id_car = models.AutoField(primary_key=True)
    nombre_car = models.CharField(max_length=100)
    fecha_creacion_car = models.DateTimeField(auto_now_add=True)
    telefono_car = models.CharField(max_length=9, blank=True, null=True)
    