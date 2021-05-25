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

#Codigo para crear la tabla de Unidades de Aprendizaje
class Unidad_de_Aprendizaje(models.Model):
    Clave=models.CharField(max_length=7,primary_key=True)
    Nombre_U=models.CharField(max_length=30)
    Posgrado=models.CharField(max_length=25)
    Tipo_U=models.CharField(max_length=10)
    Estado_U=models.CharField(max_length=10)

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

#Codigo para crear la tabla de Asignación de Unidad
class Asignacion_de_Unidad(models.Model):
    Clave_M=models.ForeignKey(Unidad_de_Aprendizaje,on_delete=models.CASCADE)
    Num_Emp=models.ForeignKey(Personal,on_delete=models.CASCADE)
    unique_together=('Clave_M','Num_Emp')
    Periodo=models.CharField(max_length=3)

#Codigo para crear la tabla de Usuario
class Usuario(models.Model):
    Usuario=models.CharField(max_length=15,primary_key=True)
    Contraseña=models.CharField(max_length=15)

#Codigo para crear la tabla de Solicitudes Colegio
class Solicitudes_Colegion(models.Model):
    Folio=models.IntegerField(primary_key=True)
    Boleta=models.ForeignKey(Alumno,on_delete=models.CASCADE)
    Num_Emp=models.ForeignKey(Personal,on_delete=models.CASCADE)
    Documento=models.FileField(upload_to='SistemaPosgrado/archivos/')
    Nombre_Tram=models.CharField(max_length=30)
    Periodo=models.CharField(max_length=3)
    Fecha=models.DateField()
    Estatus=models.CharField(max_length=11)
    Respuesta=models.FileField(upload_to='SistemaPosgrado/archivos/')

#Codigo para crear la tabla de Reportes Comité
class Reportes_Comite(models.Model):
    Clave_Comite=models.CharField(max_length=3,primary_key=True)
    Boleta=models.ForeignKey(Alumno, on_delete=models.CASCADE)
    Solicitud_Com=models.FileField(upload_to='SistemaPosgrado/archivos/')
    Fecha=models.DateField()

#Codigo para crear la tabla de Expediente Academico
class Expediente_Academico(models.Model):
    Boleta=models.ForeignKey(Alumno, on_delete=models.CASCADE)
    unique_together=('Boleta')
    Acta_alumno=models.FileField(upload_to='SistemaPosgrado/archivos/')
    CURP=models.FileField(upload_to='SistemaPosgrado/archivos/')
    Titulo=models.FileField(upload_to='SistemaPosgrado/archivos/')
    Constancia_ingles=models.FileField(upload_to='SistemaPosgrado/archivos/')







