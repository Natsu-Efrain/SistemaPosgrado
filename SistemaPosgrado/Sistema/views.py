from django.http.request import HttpHeaders, HttpRequest
from django.shortcuts import render
from django.http.response import HttpResponse
from Sistema.models import Usuario
from Sistema.models import Personal
# Create your views here.
# Prueba de commit Ian Mira
#Metodo #1 de vizualización de Login
def Costo (request):
    try:
        #Se validan si se hace una petición en el formulario de Login
        if(request.method == "POST"):
            #Se obtiene los datos ingresados en el formulario
            usuario = request.POST["Usuario"]
            password = request.POST["Password"]
            #Esta linea es igual a un Select * From Usuarios where='el nombre del usuario'
            usuarios=Usuario.objects.get(Usuario=usuario)
            #Se valida en los datos ingresados en la base de datos
            if(usuarios.Usuario==usuario and usuarios.Contraseña==password):
                   return render(request,"fallo.html")
            
    except:
        return render(request,"fallo.html")
    return render(request,"Login.html")



#Prueba
def Modulos (request):
    return render(request,"Modulos.html")


#Metodo de vizualización de AsignarU-P
def AsignarU_P (request):
    return render(request,"AsignarU-P.html")

#Metodo de vizualización de Modulos
def Modulos (request):
    return render(request,"Modulos.html")

#Metodo de vizualización de Actas
def Actas (request):
    return render(request, "Actas.html")
#Metodo Alta de Profesores
def AltaProfesores (request):
    validacion=" "
    if(request.method == "POST"):
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
        cargo="Profesor"
        #Esta linea es un insert en la tabla personal
        personal=Personal(Num_Emp=num_Emp,Nombre_P=nombre_P,Apellido_PP=apellido_PP,Apellido_MP=apellido_MP,Tipo_P=tipo_P,Correo_P=correo_P,Calle=calle,Num_Int=num_Int,Num_Ext=num_Ext,Colonia=colonia,Estado=estado,Municipio=municipio,CP=cp,Edad=edad,Sexo=sexo,Telefono=telefono,Tipo_A=tipo_A,Estado_P=estado_P,Cargo=cargo)
        personal.save()
        validacion="Exito"
    return render(request,"Alta_ Profesores.html",{"validacion":validacion})
#Metodo Baja de Profesores
def BajaProfesores (request):
    return render(request,"Baja_profesores.html")
#Metodo Calificaciones
def Calificaciones (request):
    return render(request,"Calificaciones_profesores.html")
#Metodo Estado Alumno
def EstadoAlumno (request):
    return render(request,"Est_Al.html")
#Metodo Expediente Alumno
def Expediente (request):
    return render(request,"Expediente_C.html")
#Metodo Kardex Alumno
def Kardex (request):
    return render(request,"Kardex.html")