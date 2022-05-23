from asyncore import read
from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from FamilyApp.models import Familia


def saludo(request):
    return HttpResponse("Hola coder")

def diaHoy(request):
    dia = datetime.now()
    documento_de_texto = f"El dia de hoy es {dia}"
    return HttpResponse(documento_de_texto)

def nombre(self, nombre):

    nombre = f"Nombre de la persona  es {nombre}"
    return HttpResponse(nombre)

def saludoTemplate(self):
    llamado = loader.get_template('template.html')
    documento = llamado.render()
    return HttpResponse(documento)

def saludoParametros(self):
    nom = "Leonel"
    ap = "Ieronimo"
    diccionario = {"nombre": nom, "apellido": ap}
    mi_html = open("C:/Users/USUARIO/Desktop/Programas Electronica/Phyton/EntregaPyhton/PythonMVT/PythonMVT/plantillas/templateParametros.html")
    plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context(diccionario)
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)

def saludoFamilia(self, nombreFamiliar: str = 'Nombre', edad: int = 0):
    
    plantilla = loader.get_template('templateApp.html')
    familia = Familia(nombreFamiliar = nombreFamiliar, fechaNacimiento = datetime.now(), edad = edad)
    familia.save()
    contexto =  {'familia': familia,}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)