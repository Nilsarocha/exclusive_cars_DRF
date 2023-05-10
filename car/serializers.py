# Django and DRF imports
from rest_framework import serializers

# proof class imports
from .models import Car


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"
