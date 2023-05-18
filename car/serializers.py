# Django and DRF imports
from rest_framework import serializers

# proof class imports
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class UpdateCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        read_only_field = ["id", "mileage", "price"]
