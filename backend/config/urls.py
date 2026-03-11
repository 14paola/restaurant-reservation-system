from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tables/', include('tables.urls')),
    path('api/reservations/', include('reservations.urls')),
    path('api/settings/', include('restaurant_settings.urls')),
    path('api/auth/', include('accounts.urls')),
]
