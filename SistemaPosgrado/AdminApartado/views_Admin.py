from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from AdminApartado.models_admin import Rol
from SistemaPosgrado.funciones import CargarPermisos
# Create your views here.
def Matriz_R_F(request):
    Roles=Rol.objects.all()
    Serie_ID=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    validacion=" "
    validacion_2=" "
    validacion_3=" "
    p=" "
    p1=" "
    p2=" "
    p3=" "
    p4=" "
    p5=" "
    p6=" "
    p7=" "
    p8=" "
    p9=" "
    p10=" "
    p11=" "
    p12=" "
    p13=" "
    p14=" "
    p15=" "
    p16=" "
    p17=" "
    p18=" "
    p19=" "
    if(request.method == "POST"):
        funcion=request.POST["Funcion"]
        if(funcion == "CargarPagina"):
            prueba=request.POST["Prueba"]
            (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(prueba)
            return render(request,"Matriz_R-F.html",{'Roles':Roles,'Serie':Serie_ID,'validacion':validacion,'validacion_2':validacion_2,'validacion_3':validacion_3,'validacion':validacion,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})
        elif(funcion == "Matriz"):
            for informacion in Roles:
                try:
                    Funcion=request.POST["Funcion_1"]
                    print(Funcion)
                    if(Funcion=="Agregar"):
                        #Se obtiene los datos ingresados en el formulario
                        Ag_Rol=request.POST["inputRol"]
                        if(Ag_Rol!="Titular del Departamento de Posgrado"):
                            #Esta linea es un insert en la tabla rol
                            Insert_rol=Rol(Rol=Ag_Rol)
                            Insert_rol.save()
                            validacion_2="Exito"
                            Roles=Rol.objects.all()
                        else:
                            validacion_3="Fallo"
                    elif(Funcion=="Eliminar"):
                        #Se obtiene los datos ingresados en el formulario
                        Quit_R=request.POST["inputRol"]
                        #Esta linea es un delete en la tabla rol
                        Rol.objects.filter(Rol=Quit_R).delete()
                        validacion_2="Exito"
                        Roles=Rol.objects.all()
                    elif(Funcion=="Modificar"):
                        #Se obtiene los datos ingresados en el formulario
                        p=request.POST["Prueba"]
                        Registrar_inscripci??n =request.POST[informacion.Rol+"1"]
                        Registrar_reinscripci??n=request.POST[informacion.Rol+"2"]
                        Registrar_calificaciones=request.POST[informacion.Rol+"3"]
                        Consultar_calificaciones=request.POST[informacion.Rol+"4"]
                        Cargar_solicitudes_al_Colegio=request.POST[informacion.Rol+"5"]
                        Cargar_Respuesta_solicitudes_al_Colegio=request.POST[informacion.Rol+"6"]
                        Consultar_solicitudes_al_Colegio=request.POST[informacion.Rol+"7"]
                        Cargar_reporte_del_Comit??_Tutorial=request.POST[informacion.Rol+"8"]
                        Consultar_reportes_del_Comit??_Tutorial=request.POST[informacion.Rol+"9"]
                        Consultar_alumnos_graduados_y_activos=request.POST[informacion.Rol+"10"]
                        Cargar_documentos_de_expediente_acad??mico=request.POST[informacion.Rol+"11"]
                        Registrar_profesores=request.POST[informacion.Rol+"12"]
                        Dar_de_baja_profesores=request.POST[informacion.Rol+"13"]
                        Asignar_la_Unidades_de_Aprendizaje=request.POST[informacion.Rol+"14"]
                        Crear_actas_de_calificaciones=request.POST[informacion.Rol+"15"]
                        Registrar_Unidades_de_Aprendizaje=request.POST[informacion.Rol+"16"]
                        Dar_de_baja_Unidades_de_Aprendizaje=request.POST[informacion.Rol+"17"]
                        Generar_constancias_de_inscripci??n_con_promedio_global=request.POST[informacion.Rol+"18"]
                        Generar_SIP_8BIS=request.POST[informacion.Rol+"19"]
                        #Esta linea es un modificar en la tabla rol
                        R=Rol.objects.filter(Rol=informacion.Rol).update(Registrar_inscripci??n=Registrar_inscripci??n,Registrar_reinscripci??n=Registrar_reinscripci??n,Registrar_calificaciones=Registrar_calificaciones,Cargar_solicitudes_al_Colegio=Cargar_solicitudes_al_Colegio,Consultar_calificaciones=Consultar_calificaciones,Cargar_Respuesta_solicitudes_al_Colegio=Cargar_Respuesta_solicitudes_al_Colegio,Consultar_solicitudes_al_Colegio=Consultar_solicitudes_al_Colegio,Cargar_reporte_del_Comit??_Tutorial=Cargar_reporte_del_Comit??_Tutorial,Consultar_reportes_del_Comit??_Tutorial=Consultar_reportes_del_Comit??_Tutorial,Consultar_alumnos_graduados_y_activos=Consultar_alumnos_graduados_y_activos,Cargar_documentos_de_expediente_acad??mico=Cargar_documentos_de_expediente_acad??mico,Registrar_profesores=Registrar_profesores,Dar_de_baja_profesores=Dar_de_baja_profesores,Asignar_la_Unidades_de_Aprendizaje=Asignar_la_Unidades_de_Aprendizaje,Crear_actas_de_calificaciones=Crear_actas_de_calificaciones,Registrar_Unidades_de_Aprendizaje=Registrar_Unidades_de_Aprendizaje,Dar_de_baja_Unidades_de_Aprendizaje=Dar_de_baja_Unidades_de_Aprendizaje,Generar_constancias_de_inscripci??n_con_promedio_global=Generar_constancias_de_inscripci??n_con_promedio_global,Generar_SIP_8BIS=Generar_SIP_8BIS)
                        validacion="Exito"
                        Roles=Rol.objects.all()
                        (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19)=CargarPermisos(p)
                except:
                    validacion="Fallo"
    return render(request,"Matriz_R-F.html",{'Roles':Roles,'Serie':Serie_ID,'validacion':validacion,'validacion_2':validacion_2,'validacion_3':validacion_3,'validacion':validacion,'prueba':p,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'p13':p13,'p14':p14,'p15':p15,'p16':p16,'p17':p17,'p18':p18,'p19':p19})