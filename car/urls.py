# Django and DRF imports
from rest_framework.routers import SimpleRouter

# proof class import
from .views import CarViewSet

router = SimpleRouter()

router.register(r'cars', CarViewSet, basename="cars")

urlpatterns = router.urls
