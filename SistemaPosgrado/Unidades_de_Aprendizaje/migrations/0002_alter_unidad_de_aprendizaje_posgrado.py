# Generated by Django 3.2.2 on 2021-06-01 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Unidades_de_Aprendizaje', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidad_de_aprendizaje',
            name='Posgrado',
            field=models.CharField(max_length=50),
        ),
    ]