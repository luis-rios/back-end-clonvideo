from django.shortcuts import render
from rest_framework import viewsets

from series.models import Serie
from series.serializers import SerieSerializer


class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
