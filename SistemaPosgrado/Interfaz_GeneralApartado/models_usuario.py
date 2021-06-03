from django.db import models
from AlumnosApartado.models_Alumno import Alumno
from ProfesoresApartado.models_personal import Personal
# Create your models here.
#Codigo para crear la tabla de Usuario
class Usuario(models.Model):
    Correo=models.ManyToManyField(Alumno)
    Correo=models.ManyToManyField(Personal)
    unique_together=('Correo')
    Contraseña=models.CharField(max_length=15)