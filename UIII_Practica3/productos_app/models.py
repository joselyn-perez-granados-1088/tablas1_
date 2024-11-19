from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo=models.CharField(primary_key=True,max_length=60)
    nombre=models.CharField(max_length=100)
    tipo=models.CharField(max_length=60)
    precio=models.PositiveSmallIntegerField()
    marca=models.CharField(max_length=60)
    descripcion=models.CharField(max_length=60)
    stock=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre
