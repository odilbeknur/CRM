from django.contrib import admin
from .models import Ticket, Stage, StageHistory


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "status", "created_by", "ads_info","created_at", "updated_at")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("id", "client__person__first_name", "client__person__last_name", "description")
    autocomplete_fields = ("client", "created_by")
    ordering = ("-created_at",)


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "priority","role")
    search_fields = ("name", "priority")


@admin.register(StageHistory)
class StageHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "ticket", "stage","performed_by", "completed_at")
    list_filter = ("completed_at", "stage")
    search_fields = ("ticket__id", "stage__name","performed_by__person__first_name", "performed_by__person__last_name")
    autocomplete_fields = ("ticket", "stage")
