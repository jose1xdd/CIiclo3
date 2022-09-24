from rest_framework import serializers
from medicli.models import Paciente
from .userSerializer import UserSerializer
class PacienteSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Paciente
        fields = ['cedula', 'nombre', 'apellido', 'direccion', 'telefono', 'ciudad', 'fecha', 'user']