from medicli.models.medico import Medico
from rest_framework import serializers
from medicli.serializers.userSerializer import UserSerializer

class MedicoSerializer(serializers.ModelSerializer):

    user=UserSerializer()
    class Meta:
        model = Medico
        fields = ['cedula', 'especialidad', 'nombre', 'apellido', 'direccion', 'telefono', 'ciudad', 'fecha', 'paciente']