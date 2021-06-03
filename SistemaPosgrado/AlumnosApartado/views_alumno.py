from django.shortcuts import render
from AlumnosApartado.models_Alumno import Alumno
from AlumnosApartado.models_calificaciones import Calificaciones


# Create your views here.
#Metodo Calificaciones

#Metodo Estado Alumno
def EstadoAlumno (request):
    return render(request,"Est_Al.html")

#Metodo Kardex Alumno
def Kardex (request):
    return render(request,"Kardex.html")

#Metodo Kardex Inscripción
def Reg_Alum (request):
    
    return render(request,"Reg_Alum.html")

#Metodo Reinscripción
def Reinscripcion (request):
    
    return render(request,"Reinscripcion.html")

def Registro_Calificaciones (request):
    return render(request,"Registro_Calificaciones.html")

def Est_Al (request):
    return render(request,"Est_Al.html")

def Calificacion_JCE (request):
    return render(request,"Calificacion_JCE.html")

def Calificacion_profesores (request):
    return render(request,"Calificaciones_profesores.html")

