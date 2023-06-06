# Django and DRF imports
from rest_framework.routers import SimpleRouter

# exclusive_cars import
from .views import TelevisionViewSet, FridgeViewSet

router = SimpleRouter()

router.register(r'television', TelevisionViewSet, basename="television")
router.register(r'Fridge', FridgeViewSet, basename="Fridge")

urlpatterns = router.urls
