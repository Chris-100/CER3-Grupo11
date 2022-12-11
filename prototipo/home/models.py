from django.db import models

# Create your models here.

class Recien_nacido(models.Model):
    name = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    rut = models.CharField(max_length=12)
    cupo = models.IntegerField()
    edad = models.IntegerField()
    peso = models.FloatField()
    genero = models.CharField(max_length=12)



