from django.db import models

# Create your models here.

class Recien_nacido(models.Model):
    name = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    rut = models.CharField(max_length=12)
    cupo = models.IntegerField()
    peso = models.FloatField()
    genero = models.CharField(max_length=12)
    def __str__(self) -> str:
        return super().__str__()

class Historial_medico(models.Model):
    temperatura = models.FloatField()
    estado = models.CharField(max_length=30)
    medicamento = models.CharField(max_length=300)
    via_alimentacion = models.CharField(max_length=30)
    tipo_alimentacion = models.CharField(max_length=30)
    edad = models.IntegerField()
    Rn = models.ForeignKey(Recien_nacido, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return super().__str__()



