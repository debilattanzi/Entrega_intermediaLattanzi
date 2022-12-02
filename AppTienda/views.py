from django.shortcuts import render
from .models import *


# Create your views here.
def inicio(request):
    return render(request, "inicio.html")


def proveedor(request):

    return render(request, "proveedor.html")


def prendas(request):
    return render(request, "prendas.html")


def cliente(request):
    return render(request, "cliente.html")

def formulario_cliente(request):
    return render(request, "formulario_cliente")