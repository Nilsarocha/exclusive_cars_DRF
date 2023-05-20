# Django and DRF imports
from rest_framework.viewsets import ModelViewSet

# exclusive cars import
from .serializers import ListCarSerializer, UpdateCarSerializer, CreateCarSerializer
from car.models import Car


class CarViewSet(ModelViewSet):

    queryset = Car.objects.all()
    serializer_class = ListCarSerializer
    lookup_field = "id"

    def get_serializer_class(self):
        if self.action in ["partial_update", "update"]:
            return UpdateCarSerializer
        elif self.action == "create":
            return CreateCarSerializer
        return self.serializer_class
