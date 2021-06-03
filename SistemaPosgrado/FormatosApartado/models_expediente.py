from django.db import models
from AlumnosApartado.models_Alumno import Alumno

# Create your models here.
#Codigo para crear la tabla de Expediente Academico
class Expediente_Academico(models.Model):
    Boleta=models.ForeignKey(Alumno, on_delete=models.CASCADE)
    unique_together=('Boleta')
    Acta_alumno=models.FileField(upload_to='SistemaPosgrado/archivos/')
    CURP=models.FileField(upload_to='SistemaPosgrado/archivos/')
    Titulo=models.FileField(upload_to='SistemaPosgrado/archivos/')
    Constancia_ingles=models.FileField(upload_to='SistemaPosgrado/archivos/')