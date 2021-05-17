from django.contrib import admin
from DetailsApp.models import SignUpForm

# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
	List = ['Email', 'Phone_No', 'Password']
	
admin.site.register(SignUpForm, SignUpAdmin)