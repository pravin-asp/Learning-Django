from django.contrib import admin
from crudApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	List = ['Name', 'EmpId']
	
admin.site.register(Employee, EmployeeAdmin)