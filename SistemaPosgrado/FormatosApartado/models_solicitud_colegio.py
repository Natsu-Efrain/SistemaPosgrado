from django.db import models
from AlumnosApartado.models_Alumno import Alumno
from ProfesoresApartado.models_personal import Personal
# Create your models here.
#Codigo para crear la tabla de Solicitudes Colegio
class Solicitudes_Colegio(models.Model):
    Folio=models.AutoField(primary_key=True)
    Boleta=models.ForeignKey(Alumno,on_delete=models.CASCADE)
    Num_Emp=models.ForeignKey(Personal,on_delete=models.CASCADE)
    Documento=models.FileField(upload_to='SistemaPosgrado/archivos/')
    Nombre_Tram=models.CharField(max_length=30)
    Periodo=models.CharField(max_length=3)
    Fecha=models.DateField()
    Estatus=models.CharField(max_length=11)
    Respuesta=models.FileField(upload_to='SistemaPosgrado/archivos/')