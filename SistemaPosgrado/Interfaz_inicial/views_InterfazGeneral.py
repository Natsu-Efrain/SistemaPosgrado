from django.shortcuts import render
from Interfaz_inicial.models_usuario import Usuario
from AlumnosApartado.models_Alumno import Alumno
from ProfesoresApartado.models_personal import Personal
from django.contrib.auth.models import User
from SistemaPosgrado.funciones import CargarPermisos
# Create your views here.
#Metodo de vizualización de Modulos
def Modulos (request):
    return render(request,"Modulos.html")

#Metodo de vizualización de Registro de Usuarios
def Registro_U (request):
    validacion=" "
    try:
        if(request.method == "POST"):
                #Se obtiene los datos ingresados en el formulario
                Id=request.POST["Id"]
                Usser=request.POST["Correo"]
                Password=request.POST["passwd"]
                #Se hace validacion de los datos ingresados en el formulario en la base de datos
                alumno=Alumno.objects.get(Boleta=Id)
                Rol=alumno.Rol
                if(alumno.Correo == Usser):
                        user = User.objects.create_user(Usser,'',Password)
                        user.first_name = Rol
                        usuario=Usuario(Usser,Password,Rol)
                        usuario.save()
                        user.save()
                        validacion="Exito"
                else:
                        validacion="Fallo"
    except:
        try:
                #Se hace validacion de los datos ingresados en el formulario en la base de datos
                personal=Personal.objects.get(Num_Emp=Id)
                if(personal.Correo == Usser):
                        user = User.objects.create_user(Usser,'',Password)
                        usuario=Usuario(Usser,Password)
                        usuario.save()
                        user.save()
                        validacion="Exito"
                else:
                        validacion="Fallo"
        except:
            validacion="Fallo"
    return render(request,"registro_usuarios.html",{'validacion':validacion})

def Recuperar_contraseña (request):
    return render(request,"recuperar_contraseña.html")

def Menu_P_JCE (request):
    return render(request,"Menu P_JCE.html")

def Menu_P_Prof (request):
    return render(request,"Menu P_Prof.html")

def Menu_P_A (request):
    if(request.method == "POST"):
        funcion=request.POST["Funcion"]
        if(funcion=="CargarPagina"):
            prueba=request.POST["Prueba"]
            (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
            return render(request,"Menu_P_A.html",{'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
    return render(request,"Menu_P_A.html")

def Menu_P_Cor (request):
    return render(request,"Menu_P_Cor.html")

def Menu_P_Dep (request):
    return render(request,"Menu_P_Dep.html")

def Menu_P_SP (request):
    return render(request,"Menu_P_SP.html")

def SideBar (request):
    return render(request,"SideBar.html")



