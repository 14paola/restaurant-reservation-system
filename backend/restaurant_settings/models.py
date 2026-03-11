from django.db import models

class RestaurantSettings(models.Model):
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    reservation_interval = models.PositiveIntegerField(default=30)
    reservation_duration = models.PositiveIntegerField(default=90)

    class Meta:
        verbose_name = 'Configuración del restaurante'
        verbose_name_plural = 'Configuración del restaurante'

    def __str__(self):
        return "Configuración del restaurante"