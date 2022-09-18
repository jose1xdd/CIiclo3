from django.db import models
from .user import User


class Signos_vitales(models.Model):
    ID = models.IntegerField(primary_key=True)
    Fecha_Toma = models.DateField()
    Oximetria = models.CharField(max_length=20)
    Frecuencia_Respiraoria = models.CharField(max_length=20)
    Frecuencia_cardiaca= models.CharField(max_length=20)
    Temperatura= models.CharField(max_length=20)
    Presion_Arterial = models.CharField(max_length=20)
    Glicemia = models.CharField(max_length=20)