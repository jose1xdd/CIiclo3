from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from medicli.models import Diagnostico, diagnostico
from medicli.serializers.diagnosticoSerializer import DiagnosticoSerializer

class DiagnosticoList(APIView):
    def get(self, request, format=None):
        diagnosticos = Diagnostico.objects.all()
        serializer = DiagnosticoSerializer(diagnosticos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DiagnosticoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiagnosticoDetail(APIView):

    def get_object(self, pk):
        try:
            return Diagnostico.objects.get(cedula=pk)
        except Diagnostico.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        diagnostico = self.get_object(pk)
        serializer = DiagnosticoSerializer(diagnostico)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        diagnostico = self.get_object(pk)
        serializer = DiagnosticoSerializer(diagnostico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        diagnostico = self.get_object(pk)
        diagnostico.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)