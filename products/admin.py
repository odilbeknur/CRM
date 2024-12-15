from django.contrib import admin
from .models import Product, Measurement

# Admin for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'color', 'material')  # Columns to display for Products
    search_fields = ('name', 'type', 'color', 'material')  # Search fields for Products
    list_filter = ('type', 'color', 'material')  # Filter options for Products
    ordering = ('name',)  # Default ordering for Products

# Admin for Measurement
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'product', 'height', 'width', 'description', 'photo')  # Columns to display for Measurements
    search_fields = ('ticket__id', 'product__name', 'description')  # Search fields for Measurements
    list_filter = ('product__type', 'product__color', 'product__material')  # Filter options for Measurements
    ordering = ('ticket',)  # Default ordering for Measurements

# Register the models with their admin configurations
admin.site.register(Product, ProductAdmin)
admin.site.register(Measurement, MeasurementAdmin)
