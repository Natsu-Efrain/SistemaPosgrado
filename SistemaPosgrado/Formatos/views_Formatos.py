from django.shortcuts import render
from Formatos.models_expediente import Expediente_Academico
from Formatos.models_reportes import Reportes_Comite
from Formatos.models_solicitud_colegio import Solicitudes_Colegio
# Create your views here.
#Metodo Expediente Alumno
def Expediente (request):
    return render(request,"Expediente_C.html")