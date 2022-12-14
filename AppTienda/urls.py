from django.urls import path
from AppTienda.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path('proveedor/', proveedor, name="proveedor"),
    path('prendas/', prendas, name="prendas"),
    path('cliente/', cliente, name="cliente"),
    path('busqueda_cliente/', busqueda_cliente, name="busqueda_cliente"),
    path('buscar/', buscar, name="buscar")
]
