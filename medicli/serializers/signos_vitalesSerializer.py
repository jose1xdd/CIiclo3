from medicli.models.signos_vitales import Signos_vitales
from rest_framework import serializers
from medicli.serializers.userSerializer import UserSerializer

class Signos_vitalesSerializer(serializers.ModelSerializer):
    
    user=UserSerializer()
    class Meta:
        model = Signos_vitales
        fields = ['id','fecha_toma','oximetria',
                  'frecuencia_respiratoria','frecuencia_Cardiaca','temperatura',
                  'presion_arterial','glicemia','historia']