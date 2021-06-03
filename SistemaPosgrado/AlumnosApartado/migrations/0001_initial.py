# Generated by Django 3.2.2 on 2021-06-03 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Unidades_de_AprendizajeApartado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('Boleta', models.BigIntegerField(primary_key=True, serialize=False)),
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
            name='Calificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dep_1', models.IntegerField()),
                ('Dep_2', models.IntegerField()),
                ('Dep_3', models.IntegerField()),
                ('Fecha', models.DateField()),
                ('Periodo', models.CharField(max_length=3)),
                ('Boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlumnosApartado.alumno')),
                ('Clave_M', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unidades_de_AprendizajeApartado.unidad_de_aprendizaje')),
            ],
        ),
    ]