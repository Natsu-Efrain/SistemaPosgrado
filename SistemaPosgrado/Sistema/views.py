from django.http.request import HttpHeaders, HttpRequest
from django.shortcuts import render
from django.http.response import HttpResponse
from Sistema.models import Usuario
# Create your views here.
# Prueba de commit Ian Mira
#Metodo #1 de vizualización de Login
def Login (request):
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
                return render(request,"gracias.html")
            else:
                return render(request,"fallo.html")
    except:
        return render(request,"fallo.html")
    return render(request,"Login.html")
#Metodo de vizualización de Login
def Formatos (request):
    return render(request,"Formatos.html")
#Metodo de vizualización de Actas
def Actas (request):
    return render(request, "Actas.html")
#Metodo Alta de Profesores
def AltaProfesores (request):
    return render(request,"Alta_ Profesores.html")
#Metodo Baja de Profesores
def BajaProfesores (request):
    return render(request,"Baja_profesores.html")
#Metodo Calificaciones
def Calificaciones (request):
    return render(request,"Calificaciones_profesores.html")
#Metodo Estado Alumno
def EstadoAlumno (request):
    return render(request,"Est_Al.html") 
#Metodo Expediente Alumno
def Expediente (request):
    return render(request,"Expediente_C.html") 