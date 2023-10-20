from django.db import models


class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    armafav = models.CharField(max_length=30)
    recordkill = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Arma favorita: {self.armafav} - Record de kills {self.recordkill}"


class Mapa(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Descripcion: {self.descripcion}"



class Arma(models.Model):
    nombre = models.CharField(max_length=40)
    lado = models.CharField(max_length=10)
    balas = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Lado: {self.lado} - Cantidad de balas: {self.balas}"
