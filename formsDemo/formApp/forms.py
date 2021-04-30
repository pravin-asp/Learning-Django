from django import forms

# Register your models here.

class EmployeeInfoForm(forms.Form):
	name = fomrs.CharField()
	salary = forms.IntegerField()