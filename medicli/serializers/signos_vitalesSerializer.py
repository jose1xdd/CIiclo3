from medicli.models.signos_vitales import Signos_vitales
from rest_framework import serializers

class Signos_vitalesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Signos_vitales
        fields = ['id','fecha_toma','oximetria','frecuencia_respiratoria','frecuencia_cardiaca','temperatura','presion_arterial','glicemia']

