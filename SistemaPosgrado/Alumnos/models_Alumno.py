from django.db import models

# Create your models here.
#Codigo para crear la tabla Alumno
class Alumno(models.Model):
    Boleta=models.BigIntegerField(primary_key=True)
    Nombre_A=models.CharField(max_length=25)
    Apellido_PA=models.CharField(max_length=15)
    Apellido_MA=models.CharField(max_length=15)
    Correo=models.EmailField(max_length=30)
    Calle=models.CharField(max_length=20)
    Num_Int=models.IntegerField()
    Num_Ext=models.IntegerField()
    Colonia=models.CharField(max_length=25)
    Estado=models.CharField(max_length=30)
    Municipio=models.CharField(max_length=30)
    CP=models.IntegerField()
    Posgrado=models.CharField(max_length=25)
    Edad=models.IntegerField()
    Sexo=models.CharField(max_length=1)
    Telefono=models.IntegerField()
    Tipo_A=models.CharField(max_length=10)
    Estado_A=models.CharField(max_length=10)
    Semestre=models.CharField(max_length=3)