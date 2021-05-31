from django.shortcuts import render
from Unidades_de_Aprendizaje.models_unidad_aprendizaje import Unidad_de_Aprendizaje
from Unidades_de_Aprendizaje.models_asignacion import Asignacion_de_Unidad
# Create your views here.
#Metodo de vizualización de AsignarU-P
def AsignarU_P (request):
    return render(request,"AsignarU-P.html")

