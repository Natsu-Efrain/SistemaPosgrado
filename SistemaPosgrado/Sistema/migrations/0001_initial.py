# Generated by Django 3.2.2 on 2021-05-23 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('Boleta', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre_A', models.CharField(max_length=25)),
                ('Apellido_PA', models.CharField(max_length=15)),
                ('Apellido_MA', models.CharField(max_length=15)),
                ('Correo', models.EmailField(max_length=30)),
                ('Calle', models.CharField(max_length=20)),
                ('Num_Int', models.IntegerField()),
                ('Num_Ext', models.IntegerField()),
                ('Colonia', models.CharField(max_length=25)),
                ('Estado', models.CharField(max_length=30)),
                ('Municipio', models.CharField(max_length=30)),
                ('CP', models.IntegerField()),
                ('Posgrado', models.CharField(max_length=25)),
                ('Edad', models.IntegerField()),
                ('Sexo', models.CharField(max_length=1)),
                ('Telefono', models.IntegerField()),
                ('Tipo_A', models.CharField(max_length=10)),
                ('Estado_A', models.CharField(max_length=10)),
                ('Semestre', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('Num_Emp', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('Nombre_P', models.CharField(max_length=25)),
                ('Apellido_PP', models.CharField(max_length=15)),
                ('Apellido_MP', models.CharField(max_length=15)),
                ('Tipo_P', models.CharField(max_length=2)),
                ('Correo_P', models.EmailField(max_length=30)),
                ('Calle', models.CharField(max_length=20)),
                ('Num_Int', models.IntegerField()),
                ('Num_Ext', models.IntegerField()),
                ('Colonia', models.CharField(max_length=25)),
                ('Estado', models.CharField(max_length=30)),
                ('Municipio', models.CharField(max_length=30)),
                ('CP', models.IntegerField()),
                ('Edad', models.IntegerField()),
                ('Sexo', models.CharField(max_length=1)),
                ('Telefono', models.IntegerField()),
                ('Tipo_A', models.CharField(max_length=10)),
                ('Estado_P', models.CharField(max_length=10)),
                ('Cargo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Unidad_de_Aprendizaje',
            fields=[
                ('Clave', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('Nombre_U', models.CharField(max_length=30)),
                ('Posgrado', models.CharField(max_length=25)),
                ('Tipo_U', models.CharField(max_length=10)),
                ('Estado_U', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Usuario', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('Contraseña', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitudes_Colegion',
            fields=[
                ('Folio', models.IntegerField(primary_key=True, serialize=False)),
                ('Documento', models.FileField(upload_to='SistemaPosgrado/archivos/')),
                ('Nombre_Tram', models.CharField(max_length=30)),
                ('Periodo', models.CharField(max_length=3)),
                ('Fecha', models.DateField()),
                ('Estatus', models.CharField(max_length=11)),
                ('Respuesta', models.FileField(upload_to='SistemaPosgrado/archivos/')),
                ('Boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema.alumno')),
                ('Num_Emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema.personal')),
            ],
        ),
        migrations.CreateModel(
            name='Reportes_Comite',
            fields=[
                ('Clave_Comite', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Solicitud_Com', models.FileField(upload_to='SistemaPosgrado/archivos/')),
                ('Fecha', models.DateField()),
                ('Boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Expediente_Academico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Acta_alumno', models.FileField(upload_to='SistemaPosgrado/archivos/')),
                ('CURP', models.FileField(upload_to='SistemaPosgrado/archivos/')),
                ('Titulo', models.FileField(upload_to='SistemaPosgrado/archivos/')),
                ('Constancia_ingles', models.FileField(upload_to='SistemaPosgrado/archivos/')),
                ('Boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Calificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dep_1', models.IntegerField()),
                ('Dep_2', models.IntegerField()),
                ('Dep_3', models.IntegerField()),
                ('Fecha', models.DateField()),
                ('Periodo', models.CharField(max_length=3)),
                ('Boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema.alumno')),
                ('Clave_M', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema.unidad_de_aprendizaje')),
            ],
        ),
        migrations.CreateModel(
            name='Asignacion_de_Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Periodo', models.CharField(max_length=3)),
                ('Clave_M', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema.unidad_de_aprendizaje')),
                ('Num_Emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema.personal')),
            ],
        ),
    ]
