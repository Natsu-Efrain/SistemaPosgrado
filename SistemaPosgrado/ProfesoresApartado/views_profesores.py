from django.shortcuts import render
from ProfesoresApartado.models_personal import Personal
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
#Metodo de vizualización de Actas
def Actas (request):
    return render(request, "Actas.html")
#Metodo Alta de Profesores
def AltaProfesores (request):
    validacion=" "
    try:
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
    except:
        validacion="Fallo"
    return render(request,"Alta_ Profesores.html",{"validacion":validacion})
#Metodo Baja de Profesores
def BajaProfesores (request):
    validacion=" "
    try:
        if(request.method == "POST"):
            #Se obtiene los datos ingresados en el formulario
            numero_empleado = request.POST["numero_empleado"]
            nombre = request.POST["Nom_A"]
            apellidoP = request.POST["AP_A"]
            apellidoM = request.POST["AM_A"]
            #Esta linea es igual a un Select * From Usuarios where='el nombre del usuario'
            profesor=Personal.objects.get(Num_Emp=numero_empleado,Nombre_P=nombre,Apellido_PP=apellidoP,Apellido_MP=apellidoM,Cargo='Profesor')
            profesor.Estado_P = 'Inactivo'
            profesor.save()
            validacion="Exito"
            #url = reverse('BajaProfesores_validacion', kwargs={'validacion':validacion})
            #return HttpResponseRedirect(url)
    except:
        validacion="Fallo"
        #url = reverse('BajaProfesores_validacion', kwargs={"validacion":validacion})
        #return HttpResponseRedirect(url)
    return render(request,"Baja_profesores.html",{"validacion":validacion})

#def BajaProfesores_validacion (request,validacion):
   # return render(request,"Baja_profesores.html",{"validacion":validacion})