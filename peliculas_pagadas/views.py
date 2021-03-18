from django.shortcuts import render
from rest_framework import viewsets

from peliculas_pagadas.models import Pelicula_pagada
from peliculas_pagadas.serializers import Pelicula_pagadaSerializer


class Pelicula_pagadaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula_pagada.objects.all()
    serializer_class = Pelicula_pagadaSerializer
