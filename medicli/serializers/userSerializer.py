from rest_framework import serializers
from medicli.models import User
from medicli.models import Paciente
from medicli.serializers import pacienteSerializer


class UserSerializer(serializers.ModelSerializer):
    paciente = pacienteSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'paciente']

        def create(self, validated_data):
            pacienteData = validated_data.pop('paciente')
            userInstance = User.objects.create(**validated_data)
            Paciente.objects.create(user=userInstance, **pacienteData)
            return userInstance

        def to_representation(self, obj):
            user = User.objects.get(id=obj.id)
            paciente = Paciente.objects.get(user=obj.cedula)
            return {
                'username': user.username,
                'password': user.password,
                'email': user.email,
                'paciente': {
                        'cedula':paciente.cedula, 
                        'nombre': paciente.nombre,
                        'apellido':paciente.apellido,
                        'direccion':paciente.direccion,
                        'telefono':paciente.telefono,
                        'ciudad':paciente.ciudad,
                        'fecha':paciente.fecha


                }

            }
