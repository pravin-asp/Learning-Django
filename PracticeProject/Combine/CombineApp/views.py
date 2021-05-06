from django.shortcuts import render
from . import forms, models

# Create your views here.

def FormCeration(request):
	form = forms.FormCreation()
	model = models.Models.objects.all()
	return render(request, 'CombineApp/display.html', {'forms' : form, 'model' : model})