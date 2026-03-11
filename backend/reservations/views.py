from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from .models import Reservation
from .serializers import ReservationSerializer
from .services import create_reservation, find_available_table, cancel_reservation_by_code


class ReservationAdminViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = Reservation.objects.all().order_by('date', 'time')
        date_param = self.request.query_params.get('date')
        status_param = self.request.query_params.get('status')

        if date_param:
            queryset = queryset.filter(date=date_param)

        if status_param:
            queryset = queryset.filter(status=status_param)

        return queryset


@api_view(['POST'])
@permission_classes([AllowAny])
def create_reservation_view(request):
    serializer = ReservationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        reservation = create_reservation(serializer.validated_data)
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(ReservationSerializer(reservation).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def availability_view(request):
    date = request.GET.get('date')
    time = request.GET.get('time')
    guests = request.GET.get('guests')

    if not date or not time or not guests:
        return Response(
            {'error': 'Debe enviar date, time y guests.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        from datetime import datetime
        parsed_date = datetime.strptime(date, '%Y-%m-%d').date()
        parsed_time = datetime.strptime(time, '%H:%M').time()
        parsed_guests = int(guests)

        table = find_available_table(parsed_date, parsed_time, parsed_guests)
        return Response({
            'available': True,
            'table_id': table.id,
            'table_number': table.number,
            'capacity': table.capacity
        })
    except ValueError as e:
        return Response({
            'available': False,
            'error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def cancel_reservation_view(request):
    reservation_code = request.data.get('reservation_code')

    if not reservation_code:
        return Response(
            {'error': 'Debe enviar reservation_code.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        reservation = cancel_reservation_by_code(reservation_code)
        return Response({
            'message': 'Reserva cancelada correctamente.',
            'reservation_code': str(reservation.reservation_code),
            'status': reservation.status
        })
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)