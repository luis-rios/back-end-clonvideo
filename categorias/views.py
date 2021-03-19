from django.shortcuts import render
from rest_framework import viewsets, status, response
from rest_framework.decorators import action
from rest_framework.response import Response

from categorias.models import Categoria
from categorias.serializers import CategoriaSerializer
from peliculas.serializers import PeliculaSerializer
from peliculas_pagadas.serializers import Pelicula_pagadaSerializer
from series.serializers import SerieSerializer
from series_pagadas.serializers import Serie_pagadaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    @action(methods=["GET"], detail=True)
    def peliculas(self, request, pk=None):
        categoria = self.get_object()
        if request.method == "GET":
            serializer = PeliculaSerializer(categoria.Pelicula, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(methods=["GET"], detail=True)
    def series(self, request, pk=None):
        categoria = self.get_object()
        if request == "GET":
            serializer = SerieSerializer(categoria.serie, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(methods=["GET"], detail=True)
    def series_pagadas(self, request, pk=None):
        categoria = self.get_object()
        if request.method == "GET":
            serializer = Serie_pagadaSerializer(categoria.serie_pagada, many=True)

    @action(methods=["GET"], detail=True)
    def peliculas_pagadas(self,request, pk=None):
        categoria = self.get_object()
        if request.method == "GET":
            serializer = Pelicula_pagadaSerializer(categoria.pelicula_pagada, many=True)
            return Response(status=status.HTTP_200_OK,data=serializer.data)
