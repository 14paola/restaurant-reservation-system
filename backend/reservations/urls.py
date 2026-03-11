from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ReservationAdminViewSet,
    create_reservation_view,
    availability_view,
    cancel_reservation_view,
)

router = DefaultRouter()
router.register(r'admin', ReservationAdminViewSet, basename='reservation-admin')

urlpatterns = [
    path('create/', create_reservation_view, name='create-reservation'),
    path('availability/', availability_view, name='availability'),
    path('cancel/', cancel_reservation_view, name='cancel-reservation'),
]

urlpatterns += router.urls