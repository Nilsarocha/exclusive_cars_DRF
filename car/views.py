# Django and DRF imports
import django_filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework import status, mixins
from rest_framework.response import Response

# exclusive cars import
from car.models import Car
from .serializers import (ListCarSerializer,
                          UpdateCarSerializer,
                          CreateCarSerializer,
                          ListProfileCarSerializer)


class CarViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):

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

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action == "create":
            return CreateCarSerializer
        return self.serializer_class


class MeCarView(mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                GenericViewSet):

    queryset = Car.objects.all()
    serializer_class = ListProfileCarSerializer
    lookup_field = "id"

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user.id)
        return queryset

    def get_serializer_class(self):
        if self.action in ("update", "partial_update"):
            return UpdateCarSerializer
        return self.serializer_class
