from rest_framework import serializers
from .models import RestaurantSettings

class RestaurantSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantSettings
        fields = ['id', 'opening_time', 'closing_time', 'reservation_interval', 'reservation_duration']