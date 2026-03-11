from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Table
from .serializers import TableSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all().order_by('capacity', 'number')
    serializer_class = TableSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]