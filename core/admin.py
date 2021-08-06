from django.contrib import admin
from .models import Role, Service, Employee

# Register your models here.
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
  list_display = ('role', 'is_active', 'updated_at')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
  list_display = ('service', 'icon', 'is_active', 'updated_at')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
  list_display = ('name', 'role', 'is_active', 'updated_at')