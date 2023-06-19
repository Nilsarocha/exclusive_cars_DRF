# Django and DRF imports
from rest_framework.routers import SimpleRouter

# proof class import
from .views import CarViewSet, MeCarView

router = SimpleRouter()

router.register(r'cars', CarViewSet, basename="cars")
router.register(r'me/cars', MeCarView, basename="me_cars")

urlpatterns = router.urls
