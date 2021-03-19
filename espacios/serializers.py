from rest_framework import serializers

from espacios.models import Espacio


class EspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacio
        fields = "__all__"
