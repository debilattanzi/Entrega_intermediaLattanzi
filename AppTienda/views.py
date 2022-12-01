from django.shortcuts import render


# Create your views here.
def inicio(request):
    return render(request, "inicio.html")


def proveedor(request):
    return render(request, "proveedor.html")


def prendas(request):
    return render(request, "prendas.html")
