from django.shortcuts import render, redirect
from DetailsApp import models
from DetailsApp import forms 

# Create your views here.

def Display(request):
	details = models.SignUpForm.objects.all()
	return render(request, 'DetailsApp/display.html', {'details' : details})
	
def SignUp(request):
	signup = forms.SignUpForm()
	if request.method == 'POST':
		form = forms.SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/DetailsApp/display/')
	return render(request, 'DetailsApp/signup.html', {'signup' : signup})
	
def Remove(request, id):
	data = models.SignUpForm.objects.get(id = id)
	data.delete()
	return redirect('/DetailsApp/display/')
	
def Update(request, id):
	data = models.SignUpForm.objects.get(id = id)
	if request.method == 'POST':
		form = forms.SignUpForm(request.POST, instance = data)
		if form.is_valid():
			form.save()
			return redirect('/DetailsApp/display/')
	return render(request, 'DetailsApp/edit.html', {'data' : data})