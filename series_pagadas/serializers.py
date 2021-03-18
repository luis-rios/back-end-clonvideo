from rest_framework import serializers

from series_pagadas.models import Serie_pagada


class Serie_pagadaSerializer(serializers.ModelSerializer):
    class Meta:
        model: Serie_pagada
        fields: '__all__'
