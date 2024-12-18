from django.contrib import admin
from .models import Location
# Register your models here.

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'district', 'street', 'apartment', 'entrance', 'floor', 'landmark')
    search_fields = ('city', 'district', 'street')
    list_filter = ('city', 'district')
    ordering = ('city',)