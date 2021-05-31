from django.db import models

# Create your models here.
#Codigo para crear la tabla de Unidades de Aprendizaje
class Unidad_de_Aprendizaje(models.Model):
    Clave=models.CharField(max_length=7,primary_key=True)
    Nombre_U=models.CharField(max_length=30)
    Posgrado=models.CharField(max_length=25)
    Tipo_U=models.CharField(max_length=10)
    Estado_U=models.CharField(max_length=10)

