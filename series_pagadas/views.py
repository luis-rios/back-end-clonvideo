from django.shortcuts import render
from rest_framework import viewsets

from series_pagadas.models import Serie_pagada
from series_pagadas.serializers import Serie_pagadaSerializer
from rest_framework.pagination import PageNumberPagination


class Serie_pagadaViewSet(viewsets.ModelViewSet):
    queryset = Serie_pagada.objects.all()
    serializer_class = Serie_pagadaSerializer
    pagination_class = PageNumberPagination

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
