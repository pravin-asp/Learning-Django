from django import forms 
# Create your views here.
class details(forms.Form):
	Name = forms.CharField(max_length = 10)
	Email = forms.CharField(max_length = 30)