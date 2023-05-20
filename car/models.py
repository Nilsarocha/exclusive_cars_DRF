# Phyton imports
import uuid

# Django and DRF imports
from django.db import models

# Exclusive_cars imports
from utils.models import TimestampedModel


class ColorType(models.TextChoices):
    RED = 'R', 'Rojo'
    BLUE = 'A', 'Azul'
    YELLOW = 'Am', 'Amarillo'
    BLACK = 'N', 'Negro'
    BROWN = 'M', 'Marron'
    WHITE = 'B', 'Blanco'

    @classmethod
    def get_all_choices(cls):
        return {choice.value: choice.label for choice in cls}


class Car(TimestampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.IntegerField()
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    mileage = models.IntegerField()
    price = models.FloatField()
    color = models.CharField(max_length=50, choices=ColorType.choices)
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}"
