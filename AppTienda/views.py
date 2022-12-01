from django.shortcuts import render
from .models import Cliente, Proveedor, Prendas


# Create your views here.
def inicio(request):
    return render(request, "AppTienda/inicio.html")


