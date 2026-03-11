from datetime import date, time, timedelta
from django.test import TestCase
from django.utils import timezone

from tables.models import Table
from restaurant_settings.models import RestaurantSettings
from reservations.services import find_available_table, create_reservation
from reservations.models import Reservation


class ReservationServiceTests(TestCase):
    def setUp(self):
        self.table_2 = Table.objects.create(number='1', capacity=2, is_active=True)
        self.table_4 = Table.objects.create(number='2', capacity=4, is_active=True)

        RestaurantSettings.objects.create(
            opening_time=time(12, 0),
            closing_time=time(22, 0),
            reservation_interval=30,
            reservation_duration=90
        )

        tomorrow = timezone.localdate() + timedelta(days=1)
        self.valid_date = tomorrow

    def test_find_available_table_success(self):
        table = find_available_table(
            reservation_date=self.valid_date,
            reservation_time=time(19, 0),
            guests=4
        )
        self.assertEqual(table.number, '2')

    def test_create_reservation_success(self):
        reservation = create_reservation({
            'name': 'Paola Perez',
            'email': 'paola@test.com',
            'phone': '6123-4567',
            'date': self.valid_date,
            'time': time(19, 0),
            'guests': 2
        })

        self.assertEqual(reservation.status, 'confirmed')
        self.assertEqual(Reservation.objects.count(), 1)

    def test_no_available_table(self):
        create_reservation({
            'name': 'Cliente 1',
            'email': 'c1@test.com',
            'phone': '6000-0001',
            'date': self.valid_date,
            'time': time(19, 0),
            'guests': 4
        })

        with self.assertRaisesMessage(ValueError, 'No hay disponibilidad para la fecha y hora solicitadas.'):
            create_reservation({
                'name': 'Cliente 2',
                'email': 'c2@test.com',
                'phone': '6000-0002',
                'date': self.valid_date,
                'time': time(19, 0),
                'guests': 4
            })

    def test_reservation_outside_business_hours(self):
        with self.assertRaisesMessage(ValueError, 'La reserva está fuera del horario del restaurante.'):
            find_available_table(
                reservation_date=self.valid_date,
                reservation_time=time(23, 0),
                guests=2
            )