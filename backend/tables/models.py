from django.db import models

class Table(models.Model):
    number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['capacity', 'number']
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'

    def __str__(self):
        return f"Mesa {self.number} - {self.capacity} personas"