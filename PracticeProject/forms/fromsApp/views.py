from django.shortcuts import render
from . import forms, models
# Create your views here.
def Display(request):
	form = forms.details()
	data = models.NameEmail.objects.all()
	dict = {'form' : form, 'data' : data}
	return render(request, 'formsApp/display.html', context = dict)