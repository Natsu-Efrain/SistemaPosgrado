from django.db import models
# Create your models here.
#Codigo para crear la tabla de Usuario
class Usuario(models.Model):
    Usuario=models.CharField(max_length=15,primary_key=True)
    Contraseña=models.CharField(max_length=15)