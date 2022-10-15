from django.shortcuts import render
from ejemplo.models import Familiar


def index(request):
    return render(request, "ejemplo/saludar.html", 
    {"nombre":"Yully","apellido":"Bastidas"})


def index_dos(request,nombre,apellido):
    return render(request, "ejemplo/saludar.html", 
    {
        "nombre":nombre,
        "apellido":apellido,
    })

def index_tres(request):
    return render(request, "ejemplo/saludar.html",
    {"notas":[1,2,3,4,5,6,7,8]})  

def imc(request, altura, peso): 
    imc= float(peso) / float(altura)**2
    return render(request,"ejemplo/imc.html",{"imc":imc},)

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", 
                {"lista_familiares": lista_familiares})    
    

         
