from rest_framework import serializers
from series.models import Serie


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = '__all__'
