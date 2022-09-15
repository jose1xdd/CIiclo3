from django.db import models
from .user import User


class Paciente(models.Model):
    cedula = models.CharField(primary_key=True,max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    ciudad = models.CharField(max_length=15)
    fecha = models.DateField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,
    null=False,blank=False)
