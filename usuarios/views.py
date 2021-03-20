from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from espacios.serializers import EspacioSerializer
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer
from rest_framework.pagination import PageNumberPagination


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    pagination_class = PageNumberPagination


    #paginacion y busqueda

    def get_queryset(self):
        query = {}
        for item in self.request.query_params:
            if item not in ['page_size']:
                continue
                if item in ['peliculas', 'series','peliculas_pagadas','series_pagadas']:
                    query[item + '__id'] = self.request.query_params[item]
                    continue
                query[item + '__icontains'] = self.request.query_params[item]
        self.queryset = self.queryset.filter(**query)
        return super().get_queryset()

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



