from django.shortcuts import render

# Create your views here.
#Metodo de vizualización de Modulos
def Modulos (request):
    return render(request,"Modulos.html")