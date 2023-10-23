from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from AppCsgo.models import Blog, Comentario


class NewBlog(forms.ModelForm):
    class Meta: 
        model = Blog
        fields=("titulo", "subtitulo", "cuerpo", "autor", "fecha", "imagen" )
        widgets = {
          "titulo": forms.TextInput(attrs={"class": "form-control"}),
          "subtitulo": forms.TextInput(attrs={"class": "form-control"}),
          "cuerpo": forms.Textarea(attrs={"class": "form-control"}),
          "autor": forms.TextInput(attrs={"class": "form-control", "value": "", "id":"autor_id", "type": "hidden"}),
          "fecha": forms.DateInput(attrs={"class": "form-control"}),
          "imagen": forms.FileInput(attrs={"class": "form-control"})
        }

class EditBlog(forms.ModelForm):
     class Meta: 
        model = Blog
        fields = ("titulo", "subtitulo", "cuerpo")

        widgets = {
          "titulo": forms.TextInput(attrs={"class": "form-control"}),
          "subtitulo": forms.TextInput(attrs={"class": "form-control"}),
          "cuerpo": forms.Textarea(attrs={"class": "form-control"}),
          
        }

class ComentarioNuevo(forms.ModelForm):
        class Meta: 
            model = Comentario
            fields = ('contenido',)
            widgets = {
                "autor" : forms.TextInput(attrs={"class": "form-control"}),
                "contenido" : forms.Textarea(attrs={"class": "form-control"}),
            }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        

class UserEditForm(UserCreationForm):
     email = forms.EmailField(label="Modificar E-mail")
     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
     password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
     last_name = forms.CharField()
     first_name = forms.CharField()
     class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}
