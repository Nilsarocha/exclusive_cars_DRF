# Django and DRF imports
import django_filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

# exclusive cars import
from .serializers import ListCarSerializer, UpdateCarSerializer, CreateCarSerializer
from car.models import Car


class CarViewSet(ModelViewSet):

    queryset = Car.objects.all()
    serializer_class = ListCarSerializer
    lookup_field = "id"
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        "color": ["icontains", "isnull", "exact", "in"],
        "stock": ["lt", "lte", "exact", "gte", "gt", "in"],
    }
    search_fields = ['name']
    ordering_fields = ['brand']

    def get_serializer_class(self):
        if self.action in ["partial_update", "update"]:
            return UpdateCarSerializer
        elif self.action == "create":
            return CreateCarSerializer
        return self.serializer_class
