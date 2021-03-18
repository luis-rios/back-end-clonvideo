from django.shortcuts import render
from rest_framework import viewsets

from categorias.models import Categoria
from categorias.serializers import CategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
