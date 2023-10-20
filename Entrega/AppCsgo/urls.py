from django.urls import path
from AppCsgo import views


urlpatterns = [
    path("", views.principal, name="Inicio"),
    path("formulario1/", views.jugadorFormu, name="Formulario1"),
    path("formulario2/", views.mapaFormu, name="Formulario2"),
    path("formulario3/", views.armaFormu, name="Formulario3"),
    path("busqueda1/", views.buscar, name="Busqueda"),
    path("jugadores/", views.leerJugadores, name="Leer jugadores"),
    path("eliminarjugador/<jugador_nombre>/", views.borrarjug, name="EliminarJugador"),
    path("editarjugador/<jugador_nombre>/", views.editarJug, name="EditarJugador"),
    path("mapa/list", views.leerMapas.as_view(), name="List"),
    path(r'^(?P<pk>\d+)$', views.MapaDetalle.as_view(), name="Detail"),
    path(r'^nuevo$', views.MapaCreacion.as_view(), name="New"),
    path(r'^editar/(?P<pk>\d+)$', views.MapaUpdate.as_view(), name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$', views.MapaDelete.as_view(), name="Delete"),


]
