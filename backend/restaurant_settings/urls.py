from rest_framework.routers import DefaultRouter
from .views import RestaurantSettingsViewSet

router = DefaultRouter()
router.register(r'', RestaurantSettingsViewSet, basename='restaurant-settings')

urlpatterns = router.urls