from django.shortcuts import render
from .models import *
from AppTienda.forms import *


# Create your views here.
def inicio(request):
    return render(request, "inicio.html")


def proveedor(request):
    if request.method=="POST":
        form_proveedor=ProveedorForm(request.POST)
        if form_proveedor.is_valid():
            info_proveed=form_proveedor.cleaned_data
            proveedor_nuevo=Proveedor(razon_social=info_proveed["razon_social"], cuit=info_proveed["cuit"], telefono=info_proveed["telefono"], tipo_prenda=info_proveed["tipo_prenda"])
            proveedor_nuevo.save()

            return render(request, "inicio.html", {"mensaje": "PROVEEDOR CARGADO CORRECTAMENTE"})
    else:
        form_vacio=ProveedorForm()
        return render(request, 'proveedor.html', {"form_proveedor":form_vacio})


def prendas(request):
    if request.method == "POST":
        form_prendas = PrendasForm(request.POST)
        if form_prendas.is_valid():
            info_prendas = form_prendas.cleaned_data
            prendas_nuevo = Prendas(tipo_prenda=info_prendas["tipo_prenda"], talle=info_prendas["talle"], color=info_prendas["color"])
            prendas_nuevo.save()

            return render(request, "inicio.html",{"mensaje":"PRENDA INGRESADA"})
    else:
        form_vacio = PrendasForm()
        return render(request, 'prendas.html', {"form_prendas": form_vacio})



def cliente(request):
    if request.method=="POST":
        form_cliente=ClienteForm(request.POST)
        if form_cliente.is_valid():
            info=form_cliente.cleaned_data
            cliente_nuevo=Cliente(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], celular=info["celular"])
            cliente_nuevo.save()

            return render(request, "inicio.html",{"mensaje": "CLIENTE CREADO CORRECTAMENTE"})
    else:
        form_vacio=ClienteForm()
        return render(request, "cliente.html", {"form_cliente":form_vacio})





