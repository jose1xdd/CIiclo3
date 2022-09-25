from medicli.models.enfermero import Enfermero
from rest_framework import serializers
from medicli.serializers.userSerializer import UserSerializer

class EnfermeroSerializer(serializers.ModelSerializer):

    user=UserSerializer()
    class Meta:
        model = Enfermero
        fields = ['cedula', 'nombre', 'apellido', 'direccion', 'telefono', 'ciudad', 'fecha', 'paciente']