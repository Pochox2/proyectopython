from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Blog(models.Model):
    titulo = models.CharField(max_length=25)
    subtitulo = models.CharField(max_length=30)
    cuerpo = models.TextField(null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.TextField(default=timezone.now())
    imagen = models.ImageField(null=True, blank=True, upload_to="media/")
    
    class Meta: ordering = ["titulo", "-fecha"]

    def __str__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor}"



class Comentario(models.Model):
    comentario = models.ForeignKey(Blog, related_name="comentarios", on_delete=models.CASCADE, null=True, blank=True)
    autor = models.CharField(max_length=25)
    contenido = models.TextField(null=True, blank=True)
    fecha = models.TextField(default=timezone.now())
    class Meta: ordering = ["-fecha"]
    
    def __str__(self):
        return f"Autor: {self.autor} - Contenido: {self.contenido}"
