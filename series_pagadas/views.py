from django.shortcuts import render
from rest_framework import viewsets

from series_pagadas.models import Serie_pagada
from series_pagadas.serializers import Serie_pagadaSerializer


class Serie_pagadaViewSet(viewsets.ModelViewSet):
    queryset = Serie_pagada.objects.all()
    serializer_class = Serie_pagadaSerializer
