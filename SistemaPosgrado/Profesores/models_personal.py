from django.db import models

# Create your models here.
#Codigo para crear la tabla de Personal
class Personal(models.Model):
    Num_Emp=models.CharField(max_length=15,primary_key=True)
    Nombre_P=models.CharField(max_length=25)
    Apellido_PP=models.CharField(max_length=15)
    Apellido_MP=models.CharField(max_length=15)
    Tipo_P=models.CharField(max_length=2)
    Correo_P=models.EmailField(max_length=30)
    Calle=models.CharField(max_length=20)
    Num_Int=models.IntegerField()
    Num_Ext=models.IntegerField()
    Colonia=models.CharField(max_length=25)
    Estado=models.CharField(max_length=30)
    Municipio=models.CharField(max_length=30)
    CP=models.IntegerField()
    Edad=models.IntegerField()
    Sexo=models.CharField(max_length=1)
    Telefono=models.IntegerField()
    Tipo_A=models.CharField(max_length=10)
    Estado_P=models.CharField(max_length=10)
    Cargo=models.CharField(max_length=30)