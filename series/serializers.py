from rest_framework import serializers
from rest_framework.serializers import Serializer


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model: Serializer
        fields: '__all__'
