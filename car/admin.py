# Django and DRF imports
from django.contrib import admin

# exclusive_cars imports
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('name', 'color', 'price', 'mileage', 'created_at', 'updated_at', 'deleted_at', 'active')
    list_filter = ('color', 'stock')
    search_fields = ('name', 'brand', 'model')
