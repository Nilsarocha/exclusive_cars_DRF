# Django and DRF imports
from rest_framework.routers import SimpleRouter

# exclusive_cars import
from .views import BuildingViewSet, FloorViewSet

router = SimpleRouter()

router.register(r'building', BuildingViewSet, basename="building")
router.register(r'floor', FloorViewSet, basename="floor")

urlpatterns = router.urls