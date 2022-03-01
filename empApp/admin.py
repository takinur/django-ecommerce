from django.contrib import admin
from empApp.models import Department, Employee

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ['id', 'name',]
    list_display_links = ['name']
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'department', 'designation', 'doj',]
    list_filter = ['department', 'designation', ]
    list_per_page = 10    
    list_display_links = ['name']
    search_fields = ['name', 'email', 'phone']
    
    

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
