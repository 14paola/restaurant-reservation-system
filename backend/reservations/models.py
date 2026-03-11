import uuid
from django.db import models
from tables.models import Table

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
    table = models.ForeignKey(Table, on_delete=models.PROTECT, related_name='reservations')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time']
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f"{self.name} - {self.date} {self.time} - Mesa {self.table.number}"