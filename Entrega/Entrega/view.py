from django.http import HttpResponse
from django.template import loader
from datetime import datetime


def principal(self):
    nom = "Counter Strike"
    ver = 2 
    killsx = [ 13, 14, 12, 20, 21, 22]
    diccionario ={"nombre" : nom, "version": ver, "hoy":datetime.now(), "kills" : killsx}
    plantilla = loader.get_template("plant1.html") 
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def armas(request):
        plantilla = loader.get_template("plant2.html")
        documento = plantilla.render()
        return HttpResponse(documento)

def mapas(self): 
        plantilla = loader.get_template("plant3.html")
        documento = plantilla.render()
        return HttpResponse(documento)


def formu(self): 
        plantilla = loader.get_template("plant4.html")
        documento = plantilla.render()
        return HttpResponse(documento)

def curso(self):
       curso = Curso(nombre="Desarrollo web", camada = "19881")
       curso.save()
       docTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}"

       return HttpResponse(docTexto)