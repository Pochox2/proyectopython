from django.urls import path
from AppCsgo import views

urlpatterns = [
    path("", views.principal, name="Inicio"),
    path("mapas/", views.mapas, name="Mapas"),
    path("armas/", views.armas, name="Armas"),
    path("formulario1/", views.jugadorFormu, name="Formulario1"),
    path("formulario2/", views.mapaFormu, name="Formulario2"),
    path("formulario3/", views.armaFormu, name="Formulario3"),
    path("busqueda1/", views.buscar, name="Busqueda"),

]
