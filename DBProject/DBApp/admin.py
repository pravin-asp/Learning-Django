from django.contrib import admin
from DBApp.models import Employee 

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
	emp_details = ['empNo', 'empName', 'empSalary', 'empAddress']
	
admin.site.register(Employee, EmployeeAdmin) 