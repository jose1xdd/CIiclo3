from rest_framework import serializers
from medicli.models.historia_clinica import historia_clinica
from medicli.serializers.userSerializer import UserSerializer

class historia_clinicaSerializer(serializers.ModelSerializer):
    class meta:
        model=historia_clinica
        fields=['ID','Fecha_Toma','Sugerencia']
    
