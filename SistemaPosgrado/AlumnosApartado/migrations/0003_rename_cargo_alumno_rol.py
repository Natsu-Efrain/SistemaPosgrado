# Generated by Django 3.2.2 on 2021-06-06 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AlumnosApartado', '0002_alumno_cargo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='Cargo',
            new_name='Rol',
        ),
    ]