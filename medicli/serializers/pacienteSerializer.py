from rest_framework import serializers
from medicli.models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['cedula', 'nombre', 'apellido', 'direccion', 'telefono', 'ciudad', 'fecha']