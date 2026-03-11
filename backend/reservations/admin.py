from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "date",
        "time",
        "guests",
        "table",
        "status",
        "created_at",
    )

    list_filter = ("date", "status", "table")

    search_fields = ("name", "email", "phone")

    def save_model(self, request, obj, form, change):
        try:
            obj.clean()  # ejecuta nuestra validación
        except ValidationError as e:
            form.add_error(None, e)
            return
        super().save_model(request, obj, form, change)