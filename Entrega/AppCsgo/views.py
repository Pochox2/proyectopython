from typing import Any
from AppCsgo.forms import *
from AppCsgo.models import Comentario, Blog
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView


def principal(self):

    plantilla = loader.get_template("inicio.html") 
    documento = plantilla.render()
    return HttpResponse(documento)


def login_request(request):

      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get("username")
                  contra = form.cleaned_data.get("password")

                  user = authenticate (username=usuario, password=contra)

                  if user is not None:
                        login(request, user)

                        return render(request, "./inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                  else: 
                        return render(request, "./inicio.html", {"mensaje": "Error: datos incorrectos"})
            else:
                        return render(request, "./inicio.html", {"mensaje": "Error: formulario erroneo"})
            
      form = AuthenticationForm()

      return render(request, "./login.html", {"form": form})


def register(request):
      if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render (request, "./inicio.html", {"mensaje": "Usuario creado"})
      else:

            form = UserRegisterForm()

      return render(request, "./registro.html", {"form":form})

def sobremi(self):
        plantilla = loader.get_template("sobremi.html")
        documento = plantilla.render()
        return HttpResponse(documento)

@login_required
def editarPerfil(request):

      usuario = request.user

      if request.method == "POST":
            miForm = UserEditForm(request.POST)
            if miForm.is_valid():

                  informacion = miForm.cleaned_data
                  if informacion["password1"] != informacion["password2"]:
                        datos = {
                              "username" : usuario.username,
                              "email" : usuario.email
                        }
                        miForm=UserEditForm(initial=datos)
                  else:
                        usuario.email = informacion ["email"]
                        usuario.set_password(informacion ["password1"])
                        usuario.set_password(informacion ["password2"])
                        usuario.last_name = informacion ["last_name"]
                        usuario.first_name = informacion ["first_name"]
                        usuario.save()

                  return render(request, "./inicio.html")
            
      else:
            miForm = UserEditForm(initial={ "email": usuario.email, "first_name":usuario.first_name, "last_name":usuario.last_name})

      return render(request, "./editarPerfil.html", {"miForm": miForm})

class leerBlogs(LoginRequiredMixin, ListView): 
        model = Blog
        context_object_name = "blog"
        template_name = "./blogs_list.html"

class BlogDetalle(LoginRequiredMixin, DetailView):
      model = Blog
      context_object_name = "blog"
      template_name = "./blog_detalle.html"

      def get_context_data(self, **kwargs):
       contexto = super().get_context_data(**kwargs)
       contexto ['usuario'] = self.request.user
       return contexto

class BlogCreacion(LoginRequiredMixin, CreateView):
      model = Blog
      form_class = NewBlog
      template_name = "./blog_form.html"
      success_url = reverse_lazy("List")
      def form_valid(self, form):
            form.instance.autor = self.request.user
            return super(BlogCreacion, self).form_valid(form)
      
class BlogUpdate(LoginRequiredMixin, UpdateView):
      model = Blog
      template_name = "./blog_form1.html" 
      success_url = reverse_lazy("List")
      fields = ["titulo", "subtitulo", "cuerpo" , "autor", "fecha", "imagen"]

      def get_object(self, queryset=None):
            blog = super(BlogUpdate, self).get_object()
            if blog.autor == self.request.user:
                  return blog
            else: 
                  raise Http404("Este usuario no tiene los permisos necesarios para editar este blog")
            
class BlogDelete(LoginRequiredMixin,  DeleteView):
      model = Blog
      success_url = reverse_lazy("List")

      def get_object(self, queryset=None):
            blog = super(BlogDelete, self).get_object()
            if blog.autor == self.request.user:
                  return blog
            else: 
                  raise Http404("Este usuario no tiene los permisos necesarios para eliminar este blog")

class comentariox(LoginRequiredMixin, CreateView):
      model = Comentario
      form_class = ComentarioNuevo
      template_name = "./comentarios.html"
      success_url = reverse_lazy("Inicio")

      def form_valid(self, form):
            form.instance.comentario_id = self.kwargs["pk"]
            form.instance.autor = self.request.user.username
            return super(comentariox, self).form_valid(form)
      


