from django.shortcuts import render
from . import forms
# Create your views here.
def FormCreation(response):
	form = forms.LoginDetails()
	dict = {'form' : form}
	return render(response, 'formApp/display.html', context = dict)