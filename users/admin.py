from django.contrib import admin
from .models import Role, Person, Employee, Client

# Registering Role model
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['position', 'system_user']
    search_fields = ['position', 'system_user']
    list_filter = ['system_user']

# Registering Person model
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'nickname', 'gender', 'phone_number_1', 'phone_number_2']
    search_fields = ['first_name', 'last_name', 'nickname']
    list_filter = ['gender']

# Registering Employee model
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['person', 'role', 'user']
    search_fields = ['person__first_name', 'person__last_name', 'role__position', 'user__username']
    list_filter = ['role', 'user']

# Registering Client model
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['person', 'type', 'fin_account']
    search_fields = ['person__first_name', 'person__last_name', 'type']
    list_filter = ['type']
