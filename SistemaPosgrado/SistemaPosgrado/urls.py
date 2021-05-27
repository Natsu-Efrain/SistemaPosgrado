"""SistemaPosgrado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from Interfaz_General import views_InterfazGeneral
from Alumnos import views_alumno
from Profesores import views_profesores
from Unidades_de_Aprendizaje import views_Unidad
from Formatos import views_Formatos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='Login.html'),name='login'),
    path('Logout',logout_then_login,name='logout'),
    path('Modulos/', login_required(views_InterfazGeneral.Modulos), name='Modulos'),
    path('AsignarU-P/', views_Unidad.AsignarU_P),
    path('Actas/', views_profesores.Actas),
    path('AltaProfesores/', views_profesores.AltaProfesores),
    path('BajaProfesores/', views_profesores.BajaProfesores),
    path('Calificaciones/', views_alumno.Calificaciones),
    path('EstadoAl/', views_alumno.EstadoAlumno),
    path('Expediente/', views_Formatos.Expediente),
    path('Kardex/', views_alumno.Kardex),
    
   # path('Bienvenida/', views.BienvenidaView),
    #path('Sing_up/', views.SignUpView),
]

