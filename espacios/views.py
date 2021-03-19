from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from espacios.models import Espacio
from espacios.serializers import EspacioSerializer
from peliculas.serializers import PeliculaSerializer
from peliculas_pagadas.serializers import Pelicula_pagadaSerializer
from series.serializers import SerieSerializer
from series_pagadas.serializers import Serie_pagadaSerializer


class EspacioViewSet(viewsets.ModelViewSet):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer

    @action(methods=["GET", "POST", "DELETE"], detail=True)
    def series(self, request, pk=None):
        espacio = self.get_object()

        if request.method == "GET":
            serializer = SerieSerializer(espacio.series, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method ==  "POST":
            espacio_id = request.data["serie"]
            for serie_id in espacio_id:
                serie = Espacio.objects.all(id=int(serie_id))
                espacio.serie.add(serie)
                return Response(status=status.HTTP_201_CREATED)

        if request.methos == "DELETE":
            espacio_id = request.data["serie"]
            for serie_id in espacio_id:
                serie = Espacio.objects.all(id=int(serie_id))
                espacio.serie.remove(serie)
                return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["GET", "POST", "DELETE"], detail=True)
    def peliculas(self, request, pk=None):
        espacio = self.get_object()

        if request.method == "GET":
            serializer = PeliculaSerializer(espacio.movie, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method == "POST":
            espacio_id = request.data["pelicula"]
            for pelicula_id in espacio_id:
                pelicula = Espacio.objects.all(id=int(pelicula_id))
                espacio.pelicula.add(pelicula)
                return Response(status=status.HTTP_201_CREATED)

        if request.method == "DELETE":
            espacio_id = request.data["pelicula"]
            for pelicula_id in espacio_id:
                pelicula = Espacio.objects.all(id=int(pelicula_id))
                espacio.pelicula.remove(pelicula)
                return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["GET", "POST", "DELETE"], detail=True)
    def series_pagadas(self, request, pk=None):
        espacio = self.get_object()

        if request.method == "GET":
            serializer = Serie_pagadaSerializer(espacio.paid_series, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method == "POST":
            espacio_id = request.data["serie_pagada"]
            for serie_pagada_id in espacio_id:
                serie_pagada = Espacio.objects.all(id=int(serie_pagada_id))
                espacio.serie.add(serie_pagada)
                return Response(status=status.HTTP_201_CREATED)

        if request.method == "DELETE":
            espacio_id = request.data["serie_pagada"]
            for serie_pagada_id in espacio_id:
                serie_pagada = Espacio.objects.all(id=int(serie_pagada_id))
                espacio.serie.remove(serie_pagada)
                return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["GET", "POST", "DELETE"], detail=True)
    def peliculas_pagadas(self, request, pk=None):
        espacio = self.get_object()

        if request.method == "GET":
            serializer = Pelicula_pagadaSerializer(espacio.paid_movie, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method == "POST":
            espacio_id = request.data["pelicula_pagada"]
            for pelicula_pagada_id in espacio_id:
                pelicula_pagada = Espacio.objects.all(id=int(pelicula_pagada_id))
                espacio.serie.add(pelicula_pagada)
                return Response(status=status.HTTP_201_CREATED)

        if request.method == "DELETE":
            espacio_id = request.data["pelicula_pagada"]
            for pelicula_pagada_id in espacio_id:
                pelicula_pagada = Espacio.objects.all(id=int(pelicula_pagada_id))
                espacio.serie.remove(pelicula_pagada)
                return Response(status=status.HTTP_204_NO_CONTENT)
