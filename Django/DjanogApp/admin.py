from django.contrib import admin
from . import models
# Register your models here.
class LoginAdmin(admin.ModelAdmin):
	List = ['Username', 'Password']
	
admin.site.register(models.Login, LoginAdmin)