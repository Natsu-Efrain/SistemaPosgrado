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
from AdminApartado import views_Admin
from Interfaz_inicial import views_InterfazGeneral
from AlumnosApartado import views_alumno
from ProfesoresApartado import views_profesores
from Unidades_de_AprendizajeApartado import views_Unidad
from FormatosApartado import views_Formatos


urlpatterns = [
    #Vistas del apartado de Administrador
    path('admin/', admin.site.urls),
    path('Matriz_R-F/',login_required(views_Admin.Matriz_R_F)),
    #Vistas del apartado de Interfaz Inicial
    path('accounts/login/', LoginView.as_view(template_name='Login.html'),name='login'),
    path('Logout',logout_then_login,name='logout'),
    path('Modulos/', login_required(views_InterfazGeneral.Modulos), name='Modulos'),
    path('Registro_U/',views_InterfazGeneral.Registro_U),
    path('Menu_P_A/',login_required(views_InterfazGeneral.Menu_P_A)),
    path('Recuperar_contraseña/',views_InterfazGeneral.Recuperar_contraseña),
    #Vistas del apartado Alumno
    path('EstadoAl/', login_required(views_alumno.EstadoAlumno)),
    path('Est_Al/',login_required(views_alumno.Est_Al)),
    path('Calificacion_JCE/',login_required(views_alumno.Calificacion_JCE)),
    path('Calificacion_Alumno/',login_required(views_alumno.Calificacion_profesores)),
    path('Reg_Alum/', login_required(views_alumno.Reg_Alum)),
    path('Reinscripcion/',login_required(views_alumno.Reinscripcion)),
    path('Registro_Calificaciones/',login_required(views_alumno.Registro_Calificaciones)),
    path('Kardex/', login_required(views_alumno.Kardex)),
    #Vistas del apartado Profesores
    path('AltaProfesores/', login_required(views_profesores.AltaProfesores)),
    path('BajaProfesores/', login_required(views_profesores.BajaProfesores)),
    path('Actas/', login_required(views_profesores.Actas)),
    #Vistas del apartado de Unidades
    path('AltaUnidades/', login_required(views_Unidad.AltaUnidades)),
    path('BajaUnidades/', login_required(views_Unidad.BajaUnidades)),
    path('AsignarU-P/', login_required(views_Unidad.AsignarU_P)),
    #Vistas del apartado de Formatos
    path('Formatos/',login_required(views_Formatos.Formatos)),
    path('Rep_Tu/',login_required(views_Formatos.Rep_Tu)),
    path('Expediente/', login_required(views_Formatos.Expediente)),
    path('Sol_Col_A/', login_required(views_Formatos.Sol_Col_A)),
    path('Sol_Col_P/', login_required(views_Formatos.Sol_Col_P)),
    #Vistas de pruebas
        #path('SideBar/',views_InterfazGeneral.SideBar),
        #path('Bienvenida/', views.BienvenidaView),
        #path('Sing_up/', views.SignUpView),
]

