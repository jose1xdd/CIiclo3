from rest_framework.response import Response
from rest_framework.decorators import api_view
from medicli.models import Enfermero
from medicli.serializers.enfermeroSerializer import EnfermeroSerializer

@api_view(['GET','POST'])
def EnfermeroCreateView(request):
    if request.method == 'GET':
        enfermero = Enfermero.objects.all()
        enfermero_serializer = EnfermeroSerializer(enfermero,many=True)
        return Response(enfermero_serializer.data)

    elif request.method == 'POST':
        enfermero_serializer = EnfermeroSerializer(data = request.data)
        if enfermero_serializer.is_valid():
            enfermero_serializer.save()
            return Response(enfermero_serializer.data)
        return Response(enfermero_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def EnfermeroDetailView(request,pk=None):
    
    if request.method == 'GET':
        enfermero = Enfermero.objects.filter(id = pk).first()
        enfermero_serializer = EnfermeroSerializer(enfermero)
        return Response(enfermero_serializer.data)

    elif request.method == 'PUT':
       enfermero = Enfermero.objects.filter(id = pk).first() 
       enfermero_serializer = EnfermeroSerializer(instance=enfermero, data = request.data)
       if enfermero_serializer.is_valid():
            enfermero_serializer.save()
            return Response(enfermero_serializer.data)

    elif request.method == 'DELETE':
        enfermero = Enfermero.objects.filter(id = pk).first()
        enfermero.delete()
        return Response("Eliminado...")