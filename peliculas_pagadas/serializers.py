from rest_framework import serializers

from peliculas_pagadas.models import Pelicula_pagada


class Pelicula_pagadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula_pagada
        fields = '__all__'
