from django.contrib import admin
from .models import Finance

@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'ticket', 'sum', 'remain', 'full_cost', 'created_date']
    search_fields = ['ticket__id', 'transaction']
    list_filter = ['created_date']
