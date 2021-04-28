from django.contrib import admin
from DBApp.models import Details

# Register your models here.
class AdminDetails(admin.ModelAdmin):
	details = ['Name', 'Address', 'PhoneNo', 'Pincode']
	
admin.site.register(Details, AdminDetails)