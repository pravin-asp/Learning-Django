from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def one(req):
	return HttpResponse('<h1> First Function </h1>')
	
def two(req):
	return HttpResponse('<h1> Second Function </h1>')
	
def three(req):
	return HttpResponse('<h1> Third Function </h1>')