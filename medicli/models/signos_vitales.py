from django.db import models
from .historia_clinica import Historia_clinica


class Signos_vitales(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_toma = models.DateField()
    oximetria = models.CharField(max_length=20)
    frecuencia_respiraoria = models.CharField(max_length=20)
    frecuencia_cardiaca = models.CharField(max_length=20)
    temperatura = models.CharField(max_length=20)
    presion_arterial = models.CharField(max_length=20)
    glicemia = models.CharField(max_length=20)
    historia = models.ForeignKey(
        Historia_clinica, on_delete=models.CASCADE, null=True)
