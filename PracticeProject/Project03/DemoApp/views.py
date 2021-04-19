from django.shortcuts import render
import datetime

# Create your views here.
def greeting(response):
	date = datetime.datetime.now
	d = {'DateTime' : date}
	return render(response, 'templates/practice.html', context = d)
