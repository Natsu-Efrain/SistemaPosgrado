from django.shortcuts import render
from Interfaz_inicial.models_usuario import Usuario
from AlumnosApartado.models_Alumno import Alumno
from ProfesoresApartado.models_personal import Personal
from django.contrib.auth.models import User
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
                Rol1=Alumno.objects.get(Boleta=Id)
                if(Rol1.Correo == Usser):
                        user = User.objects.create_user(Usser,'',Password)
                        usuario=Usuario(Usser,Password)
                        usuario.save()
                        user.save()
                        validacion="Exito"
                else:
                        validacion="Fallo"
    except:
        try:
                #Se hace validacion de los datos ingresados en el formulario en la base de datos
                Rol2=Personal.objects.get(Num_Emp=Id)
                if(Rol2.Correo == Usser):
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