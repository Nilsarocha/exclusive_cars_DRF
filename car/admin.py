# Django and DRF imports
from django.contrib import admin

# exclusive_cars imports
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price', 'mileage', 'created_at', 'updated_at')
    list_filter = ('color', 'stock')
    search_fields = ('name', 'brand', 'model')
