from django.db import models
from Alumnos.models_Alumno import Alumno
from Unidades_de_Aprendizaje.models_unidad_aprendizaje import Unidad_de_Aprendizaje
# Create your models here.
#Codigo para crear la tabla de Calificaciones
class Calificaciones(models.Model):
    Boleta = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    Clave_M=models.ForeignKey(Unidad_de_Aprendizaje,on_delete=models.CASCADE)
    unique_together=('Boleta','Clave_M')
    Dep_1=models.IntegerField()
    Dep_2=models.IntegerField()
    Dep_3=models.IntegerField()
    Fecha=models.DateField()
    Periodo=models.CharField(max_length=3)