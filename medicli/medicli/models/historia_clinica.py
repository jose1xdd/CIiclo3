from django.db import models
from .user import User


class Historia_clinica(models.Model):
    ID = models.IntegerField(primary_key=True)
    Fecha_Toma = models.DateField()
    Sugerencia = models.CharField(max_length =50)