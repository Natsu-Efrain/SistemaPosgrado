from django.db import models

# Create your models here.

#Codigo para crear la tabla Alumno
class Alumno(models.Model):
    Boleta=models.IntegerField(primary_key=True)
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

#Codigo para crear la tabla de Calificaciones
class Calificaciones(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    Boleta=models.IntegerField()
    Clave_M=models.CharField(max_length=7)
    unique_together=('Boleta','Clave_M')
    Dep_1=models.IntegerField()
    Dep_2=models.IntegerField()
    Dep_3=models.IntegerField()
    Fecha=models.DateField()
    Periodo=models.CharField(max_length=3)

#Codigo para crear la tabla de Unidades de Aprendizaje
class Unidad_de_Aprendizaje(models.Model):
    calificaciones=models.ForeignKey(Calificaciones,on_delete=models.CASCADE)
    Clave=models.CharField(max_length=7,primary_key=True)
    Nombre_U=models.CharField(max_length=30)
    Posgrado=models.CharField(max_length=25)
    Tipo_U=models.CharField(max_length=10)
    Estado_U=models.CharField(max_length=10)

#Codigo para crear la tabla de Asignación de Unidad
class Asignacion_de_Unidad(models.Model):
    Clave_M=models.CharField(max_length=7)
    Num_Emp=models.CharField(max_length=15)
    unique_together=('Clave_M','Num_Emp')
    Periodo=models.CharField(max_length=3)

#Codigo para crear la tabla de Personal
class Personal(models.Model):
    Num_Emp=models.CharField(max_length=15)
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




