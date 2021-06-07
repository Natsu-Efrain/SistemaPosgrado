
from Interfaz_inicial.models_usuario import Usuario
from AdminApartado.models_admin import Rol


def CargarPermisos(usuario):
    p=Usuario.objects.get(Usuario=usuario)
    pru=p.Rol
    p1=Rol.objects.get(Rol=pru)
    permiso1=p1.Registrar_inscripción
    permiso2=p1.Registrar_reinscripción
    permiso3=p1.Registrar_calificaciones
    permiso4=p1.Consultar_calificaciones
    permiso5=p1.Cargar_solicitudes_al_Colegio
    permiso6=p1.Cargar_Respuesta_solicitudes_al_Colegio
    permiso7=p1.Consultar_solicitudes_al_Colegio
    permiso8=p1.Cargar_reporte_del_Comité_Tutorial
    permiso9=p1.Consultar_reportes_del_Comité_Tutorial
    permiso10=p1.Consultar_alumnos_graduados_y_activos
    permiso11=p1.Cargar_documentos_de_expediente_académico
    permiso12=p1.Registrar_profesores
    permiso13=p1.Dar_de_baja_profesores
    permiso14=p1.Asignar_la_Unidades_de_Aprendizaje
    permiso15=p1.Crear_actas_de_calificaciones
    permiso16=p1.Registrar_Unidades_de_Aprendizaje
    permiso17=p1.Dar_de_baja_Unidades_de_Aprendizaje
    permiso18=p1.Generar_constancias_de_inscripción_con_promedio_global
    permiso19=p1.Generar_SIP_8BIS
    return permiso1,permiso2,permiso3,permiso4,permiso5,permiso6,permiso7,permiso8,permiso9,permiso10,permiso11,permiso12,permiso13,permiso14,permiso15,permiso16,permiso17,permiso18,permiso19
