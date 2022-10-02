from medicli.models import Historia_clinica
from medicli.serializers.historia_clinicaSerializer import historia_clinicaSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,views


class Historia_clinicaList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        Historia_clinica = Historia_clinica.objects.all()
        serializer = historia_clinicaSerializer(Historia_clinica, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = historia_clinicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Historia_clinicaDetail(APIView):

    def get_object(self, pk):
        try:
            return Historia_clinica.objects.get(cedula=pk)
        except Historia_clinica.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Historia_clinica = self.get_object(pk)
        serializer = historia_clinicaSerializer(medico)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Historia_clinica = self.get_object(pk)
        serializer = historia_clinicaSerializer(Historia_clinica, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Historia_clinica = self.get_object(pk)
        Historia_clinica.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)