from rest_framework.response import Response
from rest_framework.decorators import api_view
from medicli.models import Medico
from medicli.serializers.medicoSerializer import MedicoSerializer

@api_view(['GET','POST'])
def MedicoCreateView(request):

    if request.method == 'GET':
        medico = Medico.objects.all()
        medico_serializer = MedicoSerializer(medico,many=True)
        return Response(medico_serializer.data)

    elif request.method == 'POST':
        medico_serializer = MedicoSerializer(data = request.data)
        if medico_serializer.is_valid():
            medico_serializer.save()
            return Response(medico_serializer.data)
        return Response(medico_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def MedicoDetailView(request,pk=None):
    
    if request.method == 'GET':
        medico = Medico.objects.filter(id = pk).first()
        medico_serializer = MedicoSerializer(medico)
        return Response(medico_serializer.data)

    elif request.method == 'PUT':
       medico = Medico.objects.filter(id = pk).first() 
       medico_serializer = MedicoSerializer(instance=medico, data = request.data)
       if medico_serializer.is_valid():
            medico_serializer.save()
            return Response(medico_serializer.data)

    elif request.method == 'DELETE':
        medico = Medico.objects.filter(id = pk).first()
        medico.delete()
        return Response("Eliminado...")