from rest_framework import serializers
from medicli.models.historia_clinica import Historia_clinica

class historia_clinicaSerializer(serializers.ModelSerializer):
    class meta:
        model=Historia_clinica
        fields=['ID','Fecha_Toma','Sugerencia']
    
