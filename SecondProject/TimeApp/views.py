from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def tellMeTime(request):
	time = datetime.datetime.now()
	return HttpResponse('<h1> Hi the time is :' + str(time) + '</h1>')