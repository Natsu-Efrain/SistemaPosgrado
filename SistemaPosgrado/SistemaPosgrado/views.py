from django.http.request import HttpHeaders, HttpRequest
from django.shortcuts import render
from django.http.response import HttpResponse
from Interfaz_General.models_usuario import Usuario

# Create your views here.
# Prueba de commit Ian Mira
#Metodo #1 de vizualización de Login
def Costo (request):
    try:
        #Se validan si se hace una petición en el formulario de Login
        if(request.method == "POST"):
            #Se obtiene los datos ingresados en el formulario
            usuario = request.POST["Usuario"]
            password = request.POST["Password"]
            #Esta linea es igual a un Select * From Usuarios where='el nombre del usuario'
            usuarios=Usuario.objects.get(Usuario=usuario)
            #Se valida en los datos ingresados en la base de datos
            if(usuarios.Usuario==usuario and usuarios.Contraseña==password):
                   return render(request,"fallo.html")
            
    except:
        return render(request,"fallo.html")
    return render(request,"Login.html")



#Prueba
def Modulos (request):
    return render(request,"Modulos.html")






