from django.contrib import admin
from .models import Department, Employee
# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["DepartmentId", "DepartmentName"]

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["EmployeeId", "EmployeeName", "Department"]
