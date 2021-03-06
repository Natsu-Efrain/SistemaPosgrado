# Generated by Django 3.2.2 on 2021-06-03 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('Rol', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Registrar_inscripción', models.CharField(max_length=1)),
                ('Registrar_reinscripción', models.CharField(max_length=1)),
                ('Registrar_calificaciones', models.CharField(max_length=1)),
                ('Consultar_calificaciones', models.CharField(max_length=1)),
                ('Cargar_solicitudes_al_Colegio', models.CharField(max_length=1)),
                ('Cargar_Respuesta_solicitudes_al_Colegio', models.CharField(max_length=1)),
                ('Consultar_solicitudes_al_Colegio', models.CharField(max_length=1)),
                ('Cargar_reporte_del_Comité_Tutorial', models.CharField(max_length=1)),
                ('Consultar_reportes_del_Comité_Tutorial', models.CharField(max_length=1)),
                ('Consultar_alumnos_graduados_y_activos', models.CharField(max_length=1)),
                ('Cargar_documentos_de_expediente_académico', models.CharField(max_length=1)),
                ('Registrar_profesores', models.CharField(max_length=1)),
                ('Dar_de_baja_profesores', models.CharField(max_length=1)),
                ('Asignar_la_Unidades_de_Aprendizaje', models.CharField(max_length=1)),
                ('Crear_actas_de_calificaciones', models.CharField(max_length=1)),
                ('Registrar_Unidades_de_Aprendizaje', models.CharField(max_length=1)),
                ('Dar_de_baja_Unidades_de_Aprendizaje', models.CharField(max_length=1)),
                ('Generar_constancias_de_inscripción_con_promedio_global', models.CharField(max_length=1)),
                ('Generar_SIP_8BIS', models.CharField(max_length=1)),
            ],
        ),
    ]
