from django.shortcuts import render
from FormatosApartado.models_expediente import Expediente_Academico
from FormatosApartado.models_reportes import Reportes_Comite
from FormatosApartado.models_solicitud_colegio import Solicitudes_Colegio
# Create your views here.

#Metodo Expediente Sol_Col_A
def Sol_Col_A (request):
    return render(request,"Sol_Col_A.html")

#Metodo Expediente Alumno
def Sol_Col_P (request):
    return render(request,"Sol_Col_P.html")

#Metodo Expediente Alumno
def Expediente (request):
    return render(request,"Expediente_C.html")

#Metodo de vizualización de Reportes de Comité Tutorial
def Rep_Tu (request):
    return render(request,"Rep_Tu.html")
#Metodo de vizualización de Reportes de Formatos
def Formatos (request):
    return render(request,"Formatos.html")