from medicli.models.medico import Medico
from rest_framework import serializers

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['cedula', 'especialidad', 'nombre', 'apellido', 'direccion', 'telefono', 'ciudad', 'fecha', 'paciente']