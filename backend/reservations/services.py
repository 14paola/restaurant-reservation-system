from datetime import datetime, timedelta
from django.db import transaction
from django.utils import timezone
from tables.models import Table
from restaurant_settings.models import RestaurantSettings
from .models import Reservation


def get_restaurant_settings():
    settings = RestaurantSettings.objects.first()
    if not settings:
        raise ValueError("No existe configuración del restaurante.")
    return settings


def validate_reservation_datetime(reservation_date, reservation_time):
    reservation_datetime = datetime.combine(reservation_date, reservation_time)
    now = timezone.localtime()

    if timezone.is_naive(reservation_datetime):
        reservation_datetime = timezone.make_aware(reservation_datetime, timezone.get_current_timezone())

    if reservation_datetime < now:
        raise ValueError("No se puede reservar en una fecha u hora pasada.")


def validate_within_business_hours(reservation_time, settings):
    if reservation_time < settings.opening_time or reservation_time >= settings.closing_time:
        raise ValueError("La reserva está fuera del horario del restaurante.")


def find_available_table(reservation_date, reservation_time, guests):
    settings = get_restaurant_settings()

    validate_reservation_datetime(reservation_date, reservation_time)
    validate_within_business_hours(reservation_time, settings)

    candidate_tables = Table.objects.filter(
        is_active=True,
        capacity__gte=guests
    ).order_by('capacity', 'number')

    if not candidate_tables.exists():
        raise ValueError("No hay mesa con capacidad suficiente para la cantidad de invitados.")

    reservation_start = datetime.combine(reservation_date, reservation_time)
    reservation_end = reservation_start + timedelta(minutes=settings.reservation_duration)

    for table in candidate_tables:
        existing_reservations = Reservation.objects.filter(
            table=table,
            date=reservation_date,
            status='confirmed'
        )

        is_conflict = False

        for existing in existing_reservations:
            existing_start = datetime.combine(existing.date, existing.time)
            existing_end = existing_start + timedelta(minutes=settings.reservation_duration)

            if reservation_start < existing_end and reservation_end > existing_start:
                is_conflict = True
                break

        if not is_conflict:
            return table

    raise ValueError("No hay disponibilidad para la fecha y hora solicitadas.")


@transaction.atomic
def create_reservation(data):
    table = find_available_table(
        reservation_date=data['date'],
        reservation_time=data['time'],
        guests=data['guests']
    )

    reservation = Reservation.objects.create(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        date=data['date'],
        time=data['time'],
        guests=data['guests'],
        table=table,
        status='confirmed'
    )
    return reservation


def cancel_reservation_by_code(reservation_code):
    try:
        reservation = Reservation.objects.get(
            reservation_code=reservation_code,
            status='confirmed'
        )
    except Reservation.DoesNotExist:
        raise ValueError("No se encontró una reserva activa con ese código.")

    reservation.status = 'cancelled'
    reservation.save()
    return reservation