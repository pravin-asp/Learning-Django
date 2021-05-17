from django import forms
from DetailsApp import models

# Create your models here.
class SignUpForm(forms.ModelForm):
	class Meta:
		model = models.SignUpForm
		fields = '__all__'