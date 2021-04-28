from django.shortcuts import render
from DBApp.models import Details

# Create your views here.

def PrintDetails(request):
	details = Details.objects.all()
	dictionary = {'Details' : details}
	return render(request, 'templates/display.html', context = dictionary)