from rest_framework import serializers

from src.radars.models import Radar


class RadarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radar
        fields = '__all__'
