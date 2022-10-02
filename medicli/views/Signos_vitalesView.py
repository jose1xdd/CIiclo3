from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from medicli.models import Signos_vitales, signos_vitales
from medicli.serializers.signos_vitalesSerializer import Signos_vitalesSerializer

class Signos_vitalesList(APIView):
    def get(self, request, format=None):
        signos_vitales = Signos_vitales.objects.all()
        serializer = Signos_vitalesSerializer(signos_vitales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Signos_vitalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Signos_vitalesDetail(APIView):

    def get_object(self, pk):
        try:
            return Signos_vitales.objects.get(cedula=pk)
        except Signos_vitales.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        paciente = self.get_object(pk)
        serializer = Signos_vitalesSerializer(paciente)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        paciente = self.get_object(pk)
        serializer = Signos_vitalesSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        paciente = self.get_object(pk)
        paciente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)