# Generated by Django 3.2.2 on 2021-05-31 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Usuario', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('Contraseña', models.CharField(max_length=15)),
            ],
        ),
    ]
