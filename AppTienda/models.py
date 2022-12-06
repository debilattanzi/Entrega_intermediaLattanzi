from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    celular = models.IntegerField()

    def __str__(self):
        return self.nombre + " " + self.apellido


class Proveedor(models.Model):
    razon_social = models.CharField(max_length=100)
    cuit = models.IntegerField()
    telefono = models.IntegerField()
    tipo_prenda = models.CharField(max_length=50)

    def __str__(self):
        return self.razon_social


class Prendas(models.Model):
    tipo_prenda = models.CharField(max_length=50)
    talle = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_prenda
