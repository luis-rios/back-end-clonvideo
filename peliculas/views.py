from django.shortcuts import render
from rest_framework import viewsets

from peliculas.models import Pelicula
from peliculas.serializers import PeliculaSerializer
from rest_framework.pagination import PageNumberPagination




class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    pagination_class = PageNumberPagination

    # paginacion y busqueda

    def get_queryset(self):
        query = {}
        for item in self.request.query_params:
            if item not in ['page_size']:
                continue
                if item in ['peliculas']:
                    query[item + '__id'] = self.request.query_params[item]
                    continue
                query[item + '__icontains'] = self.request.query_params[item]
        self.queryset = self.queryset.filter(**query)
        return super().get_queryset()


