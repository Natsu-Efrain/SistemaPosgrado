from django.shortcuts import render
from FormatosApartado.models_expediente import Expediente_Academico
from FormatosApartado.models_reportes import Reportes_Comite
from FormatosApartado.models_solicitud_colegio import Solicitudes_Colegio
from SistemaPosgrado.funciones import CargarPermisos
# Create your views here.

#Metodo Expediente Sol_Col_A
def Sol_Col_A (request):
    return render(request,"Sol_Col_A.html")

#Metodo Expediente Alumno
def Sol_Col_P (request):
    if(request.method == "POST"):
        funcion=request.POST["Funcion"]
        if(funcion == "CargarPagina"):
            prueba=request.POST["Prueba"]
            (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
            return render(request,"Sol_Col_P.html",{'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
        else:
            return render(request,"Sol_Col_P.html")
    return render(request,"Sol_Col_P.html")


#Metodo Expediente Alumno
def Expediente (request):
    if(request.method == "POST"):
        funcion=request.POST["Funcion"]
        if(funcion == "CargarPagina"):
            prueba=request.POST["Prueba"]
            (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
            return render(request,"Expediente_C.html",{'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
        else:
            return render(request,"Expediente_C.html")
    return render(request,"Expediente_C.html")


#Metodo de vizualización de Reportes de Comité Tutorial
def Rep_Tu (request):
    if(request.method == "POST"):
        funcion=request.POST["Funcion"]
        if(funcion == "CargarPagina"):
            prueba=request.POST["Prueba"]
            (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
            return render(request,"Rep_Tu.html",{'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
        else:
            return render(request,"Rep_Tu.html")
    return render(request,"Rep_Tu.html")

#Metodo de vizualización de Reportes de Formatos
def Formatos (request):
    if(request.method == "POST"):
        funcion=request.POST["Funcion"]
        if(funcion == "CargarPagina"):
            prueba=request.POST["Prueba"]
            (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
            return render(request,"Formatos.html",{'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
        else:
            return render(request,"Formatos.html")
    return render(request,"Formatos.html")