from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppCsgo.models import Jugador, Arma, Mapa
from AppCsgo.forms import JugadorFormu, buscarJug, MapaFormu, ArmaFormu


def principal(self):

    plantilla = loader.get_template("inicio.html") 
    documento = plantilla.render()
    return HttpResponse(documento)

def armas(self):
        plantilla = loader.get_template("armas.html")
        documento = plantilla.render()
        return HttpResponse(documento)

def mapas(self): 
        plantilla = loader.get_template("mapas.html")
        documento = plantilla.render()
        return HttpResponse(documento)


def jugadorFormu(request): 
        if request.method == "POST":
               miForm = JugadorFormu(request.POST)
               print(miForm)

               if miForm.is_valid():
                informacion = miForm.cleaned_data      
                jugador = Jugador(nombre=informacion['nombre'], armafav=informacion['armafav'], recordkill=informacion['recordkill'])
                jugador.save()
                return render(request,
                      "./formulario.html")
        else:
              miForm = JugadorFormu()
        
        return render(request, "./inicio.html", {"miForm":miForm})

def armaFormu(request): 
        if request.method == "POST":
               miForm = ArmaFormu(request.POST)
               print(miForm)

               if miForm.is_valid():
                informacion = miForm.cleaned_data      
                arma = Arma(nombre=informacion['nombre'], lado=informacion['lado'], balas=informacion['balas'])
                arma.save()
                return render(request,
                      "./inicio.html")
        else:
              miForm = ArmaFormu()
        
        return render(request, "./formulario.html", {"miForm":miForm})

def mapaFormu(request): 
        if request.method == "POST":
               miForm = MapaFormu(request.POST)
               print(miForm)

               if miForm.is_valid():
                informacion = miForm.cleaned_data      
                mapa = Mapa(nombre=informacion['nombre'], descripcion=informacion['descripcion'])
                mapa.save()
                return render(request,
                      "./inicio.html")
        else:
              miForm = MapaFormu()
        
        return render(request, "./formulario.html", {"miForm":miForm})

   

def buscar(request):
      if request.method == "POST":
            miForm = buscarJug(request.POST)
            print(miForm)
            if miForm.is_valid():
                  informacion = miForm.cleaned_data
                  jugadores = Jugador.objects.filter(nombre__icontains=informacion["nombre"])
                  return render(request, "./listaj.html", {"jugadores": jugadores})
            else:
                  print("\n\n ERROR  IS_VALID FALSE \n\n")
      else:
            print(f"\n\n camino del GET \n\n")
            miForm = buscarJug()
      return render(request, "./busqueda1.html", {"miForm": miForm})