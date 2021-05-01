from django import forms

# Register your models here.

class LoginDetails(forms.Form):
	User_Name = forms.CharField(max_length = 10)
	Password = forms.CharField()