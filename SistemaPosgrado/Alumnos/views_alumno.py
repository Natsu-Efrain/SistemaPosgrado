from django.shortcuts import render
from Alumnos.models_Alumno import Alumno
from Alumnos.models_calificaciones import Calificaciones


# Create your views here.
#Metodo Calificaciones
def Calificaciones (request):
    return render(request,"Calificaciones_profesores.html")
#Metodo Estado Alumno
def EstadoAlumno (request):
    return render(request,"Est_Al.html")

#Metodo Kardex Alumno
def Kardex (request):
    return render(request,"Kardex.html")

#Metodo Kardex Inscripción
def Reg_Alum (request):
    validacion=" "
    try:
        if(request.method == "POST"):
            #Se obtiene los datos ingresados en el formulario
            Boleta=models.BigIntegerField(primary_key=True)
            Nombre_A=models.CharField(max_length=25)
            Apellido_PA=models.CharField(max_length=15)
            Apellido_MA=models.CharField(max_length=15)
            Correo=models.EmailField(max_length=30)
            Calle=models.CharField(max_length=20)
            Num_Int=models.IntegerField()
            Num_Ext=models.IntegerField()
            Colonia=models.CharField(max_length=25)
            Estado=models.CharField(max_length=30)
            Municipio=models.CharField(max_length=30)
            CP=models.IntegerField()
            Posgrado=models.CharField(max_length=25)
            Edad=models.IntegerField()
            Sexo=models.CharField(max_length=1)
            Telefono=models.IntegerField()
            Tipo_A=models.CharField(max_length=10)
            Estado_A=models.CharField(max_length=10)
            Semestre=models.CharField(max_length=3)
            Rol="Alumno"
            #Esta linea es un insert en la tabla personal
            unidad_de_aprendizaje=Unidad_de_Aprendizaje(Clave=clave,Nombre_U=nombre_U,Posgrado=posgrado,Tipo_U=tipo_U,Estado_U=estado_U)
            unidad_de_aprendizaje.save()
            validacion="Exito"
    except:
        validacion="Fallo"
    return render(request,"Reg_Alum.html",{'validacion':validacion})