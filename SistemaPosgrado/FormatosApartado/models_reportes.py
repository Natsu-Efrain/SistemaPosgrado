from django.db import models
from AlumnosApartado.models_Alumno import Alumno
# Create your models here.
#Codigo para crear la tabla de Reportes Comité
class Reportes_Comite(models.Model):
    Clave_Comite=models.CharField(max_length=3,primary_key=True)
    Boleta=models.ForeignKey(Alumno, on_delete=models.CASCADE)
    Solicitud_Com=models.FileField(upload_to='SistemaPosgrado/archivos/')
    Fecha=models.DateField()