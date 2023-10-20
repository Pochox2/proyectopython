from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class leerMapas(ListView): 
        model = Mapa
        template_name = "./mapas_list.html"

class MapaDetalle(DetailView):
      model = Mapa
      template_name = "./mapa_detalle.html"

class MapaCreacion(CreateView):
      model = Mapa
      success_url = "/AppCsgo/mapa/list"
      fields = ["nombre", "descripcion"]

class MapaUpdate(UpdateView):
      model = Mapa
      success_url = "/AppCsgo/mapa/list"
      fields = ["nombre", "descripcion"]

class MapaDelete(DeleteView):
      model = Mapa
      success_url = "/AppCsgo/mapa/list"
      


def leerJugadores(request):
      jugadores = Jugador.objects.all()


      return render(request, "./leerjugadores.html", {"jugadores": jugadores})

def borrarjug(request, jugador_nombre):
      jugador = Jugador.objects.get(nombre=jugador_nombre)
      jugador.delete()

      jugadores = Jugador.objects.all()
      contexto = {"jugadores": jugadores}

      return render (request, "./leerjugadores.html", contexto)

def editarJug(request, jugador_nombre):
      jugador = Jugador.objects.get(nombre=jugador_nombre)

      if request.method == 'POST':
            miForm = JugadorFormu(request.POST)

            print (miForm)

            if miForm.is_valid:
                  informacion = miForm.cleaned_data

                  jugador.nombre = informacion['nombre']
                  jugador.armafav = informacion['armafav']
                  jugador.recordkill = informacion['recordkill']

                  jugador.save()

                  return render(request, "./inicio.html")
            
      else:
            miForm = JugadorFormu(initial={'nombre': jugador.nombre, 'armafav': jugador.armafav, 'recordkill': jugador.recordkill})

            
            
      return render(request, "./editarJug.html", {"miForm": miForm, "jugador_nombre":jugador_nombre})

def jugadorFormu(request): 
        if request.method == 'POST':
               miForm = JugadorFormu(request.POST)
               print(miForm)

               if miForm.is_valid():
                informacion = miForm.cleaned_data      
                jugador = Jugador(nombre=informacion['nombre'], armafav=informacion['armafav'], recordkill=informacion['recordkill'])
                jugador.save()
                return render(request,
                      "./inicio.html")
        else:
              miForm = JugadorFormu()
        
        return render(request, "./formulario.html", {"miForm":miForm})

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