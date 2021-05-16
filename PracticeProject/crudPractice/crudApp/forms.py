from django import forms
from crudApp.models import Employee

class EmpForm(forms.ModelForm):
	class Meta:
		model = Employee 
		fields = '__all__'