from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from Admin.models_admin import Rol
# Create your views here.
def Matriz_R_F(request):
    Roles=Rol.objects.all()
    Serie_ID=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    validacion=" "
    for informacion in Roles:
        if(request.method == "POST"):
            try:
                #Se obtiene los datos ingresados en el formulario
                Registrar_inscripción =request.POST[informacion.Rol+"1"]
                Registrar_reinscripción=request.POST[informacion.Rol+"2"]
                Registrar_calificaciones=request.POST[informacion.Rol+"3"]
                Consultar_calificaciones=request.POST[informacion.Rol+"4"]
                Cargar_solicitudes_al_Colegio=request.POST[informacion.Rol+"5"]
                Cargar_Respuesta_solicitudes_al_Colegio=request.POST[informacion.Rol+"6"]
                Consultar_solicitudes_al_Colegio=request.POST[informacion.Rol+"7"]
                Cargar_reporte_del_Comité_Tutorial=request.POST[informacion.Rol+"8"]
                Consultar_reportes_del_Comité_Tutorial=request.POST[informacion.Rol+"9"]
                Consultar_alumnos_graduados_y_activos=request.POST[informacion.Rol+"10"]
                Cargar_documentos_de_expediente_académico=request.POST[informacion.Rol+"11"]
                Registrar_profesores=request.POST[informacion.Rol+"12"]
                Dar_de_baja_profesores=request.POST[informacion.Rol+"13"]
                Asignar_la_Unidades_de_Aprendizaje=request.POST[informacion.Rol+"14"]
                Crear_actas_de_calificaciones=request.POST[informacion.Rol+"15"]
                Registrar_Unidades_de_Aprendizaje=request.POST[informacion.Rol+"16"]
                Dar_de_baja_Unidades_de_Aprendizaje=request.POST[informacion.Rol+"17"]
                Generar_constancias_de_inscripción_con_promedio_global=request.POST[informacion.Rol+"18"]
                Generar_SIP_8BIS=request.POST[informacion.Rol+"19"]
                #Esta linea es un modificar en la tabla personal
                R=Rol.objects.filter(Rol=informacion.Rol).update(Registrar_inscripción=Registrar_inscripción,Registrar_reinscripción=Registrar_reinscripción,Registrar_calificaciones=Registrar_calificaciones,Cargar_solicitudes_al_Colegio=Cargar_solicitudes_al_Colegio,Consultar_calificaciones=Consultar_calificaciones,Cargar_Respuesta_solicitudes_al_Colegio=Cargar_Respuesta_solicitudes_al_Colegio,Consultar_solicitudes_al_Colegio=Consultar_solicitudes_al_Colegio,Cargar_reporte_del_Comité_Tutorial=Cargar_reporte_del_Comité_Tutorial,Consultar_reportes_del_Comité_Tutorial=Consultar_reportes_del_Comité_Tutorial,Consultar_alumnos_graduados_y_activos=Consultar_alumnos_graduados_y_activos,Cargar_documentos_de_expediente_académico=Cargar_documentos_de_expediente_académico,Registrar_profesores=Registrar_profesores,Dar_de_baja_profesores=Dar_de_baja_profesores,Asignar_la_Unidades_de_Aprendizaje=Asignar_la_Unidades_de_Aprendizaje,Crear_actas_de_calificaciones=Crear_actas_de_calificaciones,Registrar_Unidades_de_Aprendizaje=Registrar_Unidades_de_Aprendizaje,Dar_de_baja_Unidades_de_Aprendizaje=Dar_de_baja_Unidades_de_Aprendizaje,Generar_constancias_de_inscripción_con_promedio_global=Generar_constancias_de_inscripción_con_promedio_global,Generar_SIP_8BIS=Generar_SIP_8BIS)
                validacion="Exito"
                Roles=Rol.objects.all()
            except:
                validacion="Fallo"
    return render(request,"Matriz_R-F.html",{'Roles':Roles,'Serie':Serie_ID,'validacion':validacion})