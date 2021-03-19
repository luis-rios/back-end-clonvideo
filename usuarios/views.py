from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from espacios.serializers import EspacioSerializer
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(methods=["GET", "POST", "DELETE"], detail=True)
    def miEspacio(self, request, pk=None):
        usuario = self.get_object()

        if request.method == "GET":
            serializer = EspacioSerializer(usuario.espacio)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method == "POST":
            usuario_id= request.data["espacio"]
            for espacio_id in usuario_id:
                espacio = Usuario.objects.all(id=int(espacio_id))
                usuario.espacio.add(espacio)
                return Response(status=status.HTTP_201_CREATED)

        if request.method == "DELETE":
            usuario_id = request.data["espacio"]
            for espacio_id in usuario_id:
                espacio = Usuario.objects.all(id=int(espacio_id))
                usuario.espacio.remove(espacio)
                return Response(status=status.HTTP_204_NO_CONTENT)



