# Django and DRF imports
from rest_framework import serializers

# proof class imports
from .models import Car, ColorType


class ListCarSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = Car
        exclude = ["created_at", "updated_at", "deleted_at", "active"]


class ListProfileCarSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = Car
        fields = "__all__"


class CreateCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        color_key = representation['color']
        color_value = dict(ColorType.choices)[color_key]
        representation['color'] = color_value
        return representation


class UpdateCarSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')

    class Meta:
        model = Car
        fields = "__all__"
        read_only_field = ["id", "mileage", "price", "color"]
