from django import forms

# Create your views here.
class FormCreation(forms.Form):
	Name = forms.CharField(max_length = 20)
	DoB = forms.DateField()