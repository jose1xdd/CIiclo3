from django.db import models
from .medico import Medico
from .historia_clinica import Historia_clinica


class Diagnostico(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=150)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    historiaClinica = models.ForeignKey(
        Historia_clinica, on_delete=models.CASCADE, null=True)
    