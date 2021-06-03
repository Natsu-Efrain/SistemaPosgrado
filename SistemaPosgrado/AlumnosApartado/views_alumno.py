from django.shortcuts import render
from AlumnosApartado.models_Alumno import Alumno
from AlumnosApartado.models_calificaciones import Calificaciones


# Create your views here.
#Metodo Calificaciones
def Calificaciones (request):
    return render(request,"Calificaciones_profesores.html")
#Metodo Estado Alumno
def EstadoAlumno (request):
    return render(request,"Est_Al.html")

#Metodo Kardex Alumno
def Kardex (request):
    return render(request,"Kardex.html")

#Metodo Kardex Inscripción
def Reg_Alum (request):
    
    return render(request,"Reg_Alum.html")