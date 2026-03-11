import uuid
from datetime import datetime, timedelta

from django.db import models
from django.core.exceptions import ValidationError

from tables.models import Table
from restaurant_settings.models import RestaurantSettings


class Reservation(models.Model):

    STATUS_CHOICES = [
        ('confirmed', 'Confirmada'),
        ('cancelled', 'Cancelada'),
    ]

    reservation_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    table = models.ForeignKey(
        Table,
        on_delete=models.PROTECT,
        related_name='reservations'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='confirmed'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time']
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f"{self.name} - {self.date} {self.time} - Mesa {self.table.number}"

    # VALIDACIÓN PARA EVITAR DOBLE RESERVA DE LA MISMA MESA
    def clean(self):
        settings = RestaurantSettings.objects.first()

        if not settings:
            return

        reservation_start = datetime.combine(self.date, self.time)
        reservation_end = reservation_start + timedelta(minutes=settings.reservation_duration)

        existing_reservations = Reservation.objects.filter(
            table=self.table,
            date=self.date,
            status='confirmed'
        ).exclude(id=self.id)

        for existing in existing_reservations:
            existing_start = datetime.combine(existing.date, existing.time)
            existing_end = existing_start + timedelta(minutes=settings.reservation_duration)

            if reservation_start < existing_end and reservation_end > existing_start:
                raise ValidationError("Esta mesa ya está reservada en ese horario.")

    # EJECUTA LA VALIDACIÓN ANTES DE GUARDAR
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)