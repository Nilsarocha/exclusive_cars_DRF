# Django and DRF imports
from rest_framework.viewsets import ModelViewSet

# proof class imports
from .serializers import CarSerializer, UpdateCarSerializer
from car.models import Car


class CarViewSet(ModelViewSet):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = "id"

    def get_serializer_class(self):
        if self.action in ["partial_update", "update"]:
            return UpdateCarSerializer
        return self.serializer_class
