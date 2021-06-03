from django.db import models
from Unidades_de_AprendizajeApartado.models_unidad_aprendizaje import Unidad_de_Aprendizaje
from ProfesoresApartado.models_personal import Personal
# Create your models here.
#Codigo para crear la tabla de Asignación de Unidad
class Asignacion_de_Unidad(models.Model):
    Clave_M=models.ForeignKey(Unidad_de_Aprendizaje,on_delete=models.CASCADE)
    Num_Emp=models.ForeignKey(Personal,on_delete=models.CASCADE)
    unique_together=('Clave_M','Num_Emp')
    Periodo=models.CharField(max_length=3)