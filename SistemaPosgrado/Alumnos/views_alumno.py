from django.shortcuts import render

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