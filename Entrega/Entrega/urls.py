from django.contrib import admin
from django.urls import path
from Entrega.view import principal, mapas, armas, curso

urlpatterns = [
    path('admin/', admin.site.urls),
    path("csgo/", principal),
    path("mapas/", mapas),
    path("armas/", armas),
    path("curso/", curso)
]
