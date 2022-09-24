from medicli.models.enfermero import Enfermero
from rest_framework import serializers

class EnfermeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermero
        fields = ['cedula', 'nombre', 'apellido', 'direccion', 'telefono', 'ciudad', 'fecha', 'paciente']