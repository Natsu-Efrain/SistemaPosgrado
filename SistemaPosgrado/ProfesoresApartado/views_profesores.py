from django.shortcuts import render
from ProfesoresApartado.models_personal import Personal
from django.urls import reverse
from django.http import HttpResponseRedirect
from SistemaPosgrado.funciones import CargarPermisos
# Create your views here.
#Metodo de vizualización de Actas
def Actas (request):
    if(request.method == "POST"):
        funcion=request.POST["Funcion"]
        if(funcion == "CargarPagina"):
            prueba=request.POST["Prueba"]
            (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
            return render(request,"Actas.html",{'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
        else:
            return render(request, "Actas.html")
    return render(request, "Actas.html")
#Metodo Alta de Profesores
def AltaProfesores (request):
    validacion=" "
    if(request.method == "POST"):
        funcion=request.POST["Funcion"]
        if(funcion == "CargarPagina"):
            prueba=request.POST["Prueba"]
            (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
            return render(request,"Alta_ Profesores.html",{'validacion':validacion,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
        elif(funcion == "Registrar"):
            try:
                    #Se obtiene los datos ingresados en el formulario
                    num_Emp=request.POST["numero_empleado"]
                    nombre_P=request.POST["nombre"]
                    apellido_PP=request.POST["apellidoP"]
                    apellido_MP=request.POST["apellidoM"]
                    tipo_P=request.POST["tipo"]
                    correo_P=request.POST["correo"]
                    calle=request.POST["calle"]
                    num_Int=request.POST["numero_interior"]
                    num_Ext=request.POST["numero_exterior"]
                    colonia=request.POST["colonia"]
                    estado=request.POST["estado"]
                    municipio=request.POST["municipio"]
                    cp=request.POST["codigo_postal"]
                    edad=request.POST["edad"]
                    sexo=request.POST["sexo"]
                    telefono=request.POST["telefono"]
                    tipo_A=request.POST["tipo"]
                    estado_P="Activo"
                    rol="Profesor"
                    #Esta linea es un insert en la tabla personal
                    personal=Personal(Num_Emp=num_Emp,Nombre_P=nombre_P,Apellido_PP=apellido_PP,Apellido_MP=apellido_MP,Tipo_P=tipo_P,Correo=correo_P,Calle=calle,Num_Int=num_Int,Num_Ext=num_Ext,Colonia=colonia,Estado=estado,Municipio=municipio,CP=cp,Edad=edad,Sexo=sexo,Telefono=telefono,Tipo_A=tipo_A,Estado_P=estado_P,Rol=rol)
                    personal.save()
                    validacion="Exito"
                    prueba=request.POST["Prueba"]
                    (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
                    return render(request,"Alta_ Profesores.html",{'validacion':validacion,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
            except:
                validacion="Fallo"
    return render(request,"Alta_ Profesores.html",{"validacion":validacion})

#Metodo Baja de Profesores
def BajaProfesores (request):
    validacion=" "
    if(request.method == "POST"):
        funcion=request.POST["Funcion"]
        if(funcion == "CargarPagina"):
            prueba=request.POST["Prueba"]
            (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
            return render(request,"Baja_Profesores.html",{'validacion':validacion,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
        elif(funcion == "Modificar"):
            try:
                    #Se obtiene los datos ingresados en el formulario
                    numero_empleado = request.POST["numero_empleado"]
                    nombre = request.POST["Nom_A"]
                    apellidoP = request.POST["AP_A"]
                    apellidoM = request.POST["AM_A"]
                    #Esta linea es igual a un Select * From Usuarios where='el nombre del usuario'
                    profesor=Personal.objects.get(Num_Emp=numero_empleado,Nombre_P=nombre,Apellido_PP=apellidoP,Apellido_MP=apellidoM,Rol='Profesor')
                    profesor.Estado_P = 'Inactivo'
                    profesor.save()
                    validacion="Exito"
                    prueba=request.POST["Prueba"]
                    (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
                    return render(request,"Baja_Profesores.html",{'validacion':validacion,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
            except:
                validacion="Fallo"
    return render(request,"Baja_Profesores.html",{"validacion":validacion})