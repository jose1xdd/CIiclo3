from django.db import models
from .user import User


class Diagnostico(models.Model):
    diagnostico = models.CharField(primary_key=True,max_length=20)
    descripcion = models.CharField(max_length=150)
