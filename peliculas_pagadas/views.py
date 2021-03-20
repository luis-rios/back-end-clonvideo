from django.shortcuts import render
from rest_framework import viewsets

from peliculas_pagadas.models import Pelicula_pagada
from peliculas_pagadas.serializers import Pelicula_pagadaSerializer


class Pelicula_pagadaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula_pagada.objects.all()
    serializer_class = Pelicula_pagadaSerializer

    # paginacion y busqueda
    def get_queryset(self):
        query = {}
        for item in self.request.query_params:
            if item not in ['page_size']:
                continue
                if item in ['peliculas_pagadas']:
                    query[item + '__id'] = self.request.query_params[item]
                    continue
                query[item + '__icontains'] = self.request.query_params[item]
        self.queryset = self.queryset.filter(**query)
        return super().get_queryset()