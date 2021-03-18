from django.shortcuts import render
from rest_framework import viewsets

from espacios.models import Espacio
from espacios.serializers import EspacioSerializer


class EspacioViewSet(viewsets.ModelViewSet):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer
