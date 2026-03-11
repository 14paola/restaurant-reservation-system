from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    table_number = serializers.CharField(source='table.number', read_only=True)
    reservation_code = serializers.UUIDField(read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'id',
            'reservation_code',
            'name',
            'email',
            'phone',
            'date',
            'time',
            'guests',
            'table',
            'table_number',
            'status',
            'created_at',
        ]
        read_only_fields = ['table', 'status', 'created_at']