from django import forms

class JugadorFormu(forms.Form):
    nombre = forms.CharField(max_length=40)
    armafav = forms.CharField(max_length=30)
    recordkill = forms.IntegerField()

class ArmaFormu(forms.Form):
    nombre = forms.CharField(max_length=40)
    lado = forms.CharField(max_length=30)
    balas = forms.IntegerField()

class MapaFormu(forms.Form):
        nombre = forms.CharField(max_length=20)
        descripcion = forms.CharField(max_length=40)


class buscarJug(forms.Form):
    nombre = forms.CharField()

