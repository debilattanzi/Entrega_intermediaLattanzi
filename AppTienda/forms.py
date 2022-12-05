from django import forms

class ClienteForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    celular=forms.IntegerField()

class ProveedorForm(forms.Form):
    razon_social = forms.CharField(max_length=100)
    cuit = forms.IntegerField()
    telefono = forms.IntegerField()
    tipo_prenda = forms.CharField(max_length=50)

class PrendasForm(forms.Form):
    tipo_prenda = forms.CharField(max_length=50)
    talle = forms.IntegerField()
    color = forms.CharField(max_length=50)