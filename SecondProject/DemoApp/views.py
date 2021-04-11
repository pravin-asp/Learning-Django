from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def goodMorning_view(response):
	return HttpResponse('<h1> Good Morning </h1>')
	
def goodAfternoon_view(response):
	return HttpResponse('<h1> Good Afternoon </h1>')

def goodEvening_view(response):
	return HttpResponse('<h1> Good Evening </h1>')
