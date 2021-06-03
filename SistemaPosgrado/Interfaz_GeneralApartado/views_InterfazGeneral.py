from django.shortcuts import render
from Interfaz_GeneralApartado.models_usuario import Usuario
# Create your views here.
#Metodo de vizualización de Modulos
def Modulos (request):
    return render(request,"Modulos.html")

#Metodo de vizualización de Registro de Usuarios
def Registro_U (request):
    return render(request,"registro_usuarios.html")