from medicli.models.familiar import Familiar
from rest_framework import serializers

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ['cedula', 'nombre', 'apellido', 'parentesco', 'direccion', 'telefono', 'ciudad', 
        'fecha']