from django.contrib import admin
from .models import RestaurantSettings

@admin.register(RestaurantSettings)
class RestaurantSettingsAdmin(admin.ModelAdmin):
    list_display = ('opening_time', 'closing_time', 'reservation_interval', 'reservation_duration')