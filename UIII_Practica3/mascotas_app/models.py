from django.db import models
# Create your models here.

class Mascota(models.Model):
    codigo=models.CharField(primary_key=True,max_length=60)
    especie=models.CharField(max_length=100)
    tamaño=models.CharField(max_length=60)
    precio=models.PositiveSmallIntegerField()
    dieta=models.CharField(max_length=60)
    temperamento=models.CharField(max_length=60)
    cuidados=models.CharField(max_length=60)
    edad=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre
