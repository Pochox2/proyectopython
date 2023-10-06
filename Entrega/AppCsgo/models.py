from django.db import models


class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    armafav = models.CharField(max_length=30)
    recordkill = models.IntegerField()


class Mapa(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)



class Arma(models.Model):
    nombre = models.CharField(max_length=40)
    lado = models.CharField(max_length=10)
    balas = models.IntegerField()
