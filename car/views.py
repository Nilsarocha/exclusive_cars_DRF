# Django and DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# proof class imports
from .serializers import CarSerializer
from car.models import Car


class CarViewSet(GenericViewSet):

    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
