from django.shortcuts import render
from Unidades_de_AprendizajeApartado.models_unidad_aprendizaje import Unidad_de_Aprendizaje
from Unidades_de_AprendizajeApartado.models_asignacion import Asignacion_de_Unidad
from SistemaPosgrado.funciones import CargarPermisos
# Create your views here.
#Metodo de vizualización de AsignarU-P
def AsignarU_P (request):
    if(request.method == "POST"):
        funcion=request.POST["Funcion"]
        if(funcion == "CargarPagina"):
            prueba=request.POST["Prueba"]
            (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
            return render(request,"AsignarU-P.html",{'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
        else:
            return render(request,"AsignarU-P.html")
    return render(request,"AsignarU-P.html")
#Metodo de vizualización de Altas de Unidades de aprendizaje
def AltaUnidades (request):
    validacion=" "
    if(request.method == "POST"):
        funcion=request.POST["Funcion"]
        if(funcion == "CargarPagina"):
            prueba=request.POST["Prueba"]
            (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
            return render(request,"unidades_aprendizaje_alta.html",{'validacion':validacion,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
        elif(funcion == "Registrar"):
            try:
                    #Se obtiene los datos ingresados en el formulario
                    clave=request.POST["Clave"]
                    nombre_U=request.POST["Nombre_U"]
                    posgrado=request.POST["Posgrado"]
                    tipo_U=request.POST["Tipo_U"]
                    estado_U="Activo"
                    #Esta linea es un insert en la tabla personal
                    unidad_de_aprendizaje=Unidad_de_Aprendizaje(Clave=clave,Nombre_U=nombre_U,Posgrado=posgrado,Tipo_U=tipo_U,Estado_U=estado_U)
                    unidad_de_aprendizaje.save()
                    validacion="Exito"
                    prueba=request.POST["Prueba"]
                    (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
                    return render(request,"unidades_aprendizaje_alta.html",{'validacion':validacion,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
            except:
                validacion="Fallo"
    return render(request,"unidades_aprendizaje_alta.html",{'validacion':validacion})

#Metodo de vizualización de Baja de Unidades de aprendizaje
def BajaUnidades (request):
    validacion=" "
    if(request.method == "POST"):
        funcion=request.POST["Funcion"]
        if(funcion == "CargarPagina"):
            prueba=request.POST["Prueba"]
            (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
            return render(request,"unidades_aprendizaje_bajas.html",{'validacion':validacion,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
        elif(funcion == "Modificar"):
            try:
                #Se obtiene los datos ingresados en el formulario
                clave=request.POST["Clave"]
                nombre_U=request.POST["Nombre_U"]
                #Esta linea es igual a un Select * From Usuarios where='el nombre del usuario'
                unidad_de_aprendizaje=Unidad_de_Aprendizaje.objects.get(Clave=clave,Nombre_U=nombre_U)
                unidad_de_aprendizaje.Estado_U = 'Inactivo'
                unidad_de_aprendizaje.save()
                validacion="Exito"
                prueba=request.POST["Prueba"]
                (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
                return render(request,"unidades_aprendizaje_bajas.html",{'validacion':validacion,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
            except:
                validacion="Fallo"
    return render(request,"unidades_aprendizaje_bajas.html",{'validacion':validacion})

