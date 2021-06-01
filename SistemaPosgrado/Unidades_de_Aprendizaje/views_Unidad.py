from django.shortcuts import render
from Unidades_de_Aprendizaje.models_unidad_aprendizaje import Unidad_de_Aprendizaje
from Unidades_de_Aprendizaje.models_asignacion import Asignacion_de_Unidad
# Create your views here.
#Metodo de vizualización de AsignarU-P
def AsignarU_P (request):
    return render(request,"AsignarU-P.html")
#Metodo de vizualización de Altas de Unidades de aprendizaje
def AltaUnidades (request):
    validacion=" "
    try:
        if(request.method == "POST"):
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
    except:
        validacion="Fallo"
    return render(request,"unidades_aprendizaje_alta.html",{'validacion':validacion})

#Metodo de vizualización de Baja de Unidades de aprendizaje
def BajaUnidades (request):
    validacion=" "
    try:
        if(request.method == "POST"):
            #Se obtiene los datos ingresados en el formulario
            clave=request.POST["Clave"]
            nombre_U=request.POST["Nombre_U"]
            #Esta linea es igual a un Select * From Usuarios where='el nombre del usuario'
            unidad_de_aprendizaje=Unidad_de_Aprendizaje.objects.get(Clave=clave,Nombre_U=nombre_U)
            unidad_de_aprendizaje.Estado_U = 'Inactivo'
            unidad_de_aprendizaje.save()
            validacion="Exito"
            #url = reverse('BajaProfesores_validacion', kwargs={'validacion':validacion})
            #return HttpResponseRedirect(url)
    except:
        validacion="Fallo"
        #url = reverse('BajaProfesores_validacion', kwargs={"validacion":validacion})
        #return HttpResponseRedirect(url)
    return render(request,"unidades_aprendizaje_bajas.html",{'validacion':validacion})

