from django.shortcuts import render
from Formatos.models_expediente import Expediente_Academico
from Formatos.models_reportes import Reportes_Comite
from Formatos.models_solicitud_colegio import Solicitudes_Colegio
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