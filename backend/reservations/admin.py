from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'guests', 'table', 'status', 'created_at')
    readonly_fields = ('reservation_code', 'created_at')