from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import RestaurantSettings
from .serializers import RestaurantSettingsSerializer

class RestaurantSettingsViewSet(viewsets.ModelViewSet):
    queryset = RestaurantSettings.objects.all()
    serializer_class = RestaurantSettingsSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]