from django.shortcuts import render

# Create your views here.
#Metodo Expediente Alumno
def Expediente (request):
    return render(request,"Expediente_C.html")