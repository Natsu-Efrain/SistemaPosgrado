from django.shortcuts import render
from Interfaz_General.models_usuario import Usuario
# Create your views here.
#Metodo de vizualización de Modulos
def Modulos (request):
    return render(request,"Modulos.html")