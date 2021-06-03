# Generated by Django 3.2.2 on 2021-06-03 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProfesoresApartado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad_de_Aprendizaje',
            fields=[
                ('Clave', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('Nombre_U', models.CharField(max_length=30)),
                ('Posgrado', models.CharField(max_length=100)),
                ('Tipo_U', models.CharField(max_length=10)),
                ('Estado_U', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Asignacion_de_Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Periodo', models.CharField(max_length=3)),
                ('Clave_M', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unidades_de_AprendizajeApartado.unidad_de_aprendizaje')),
                ('Num_Emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProfesoresApartado.personal')),
            ],
        ),
    ]
