from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fun1(request):
	return HttpResponse('<h1> Function 01 </h1>')
	
def fun2(request):
	return HttpResponse('<h2> Function 02 </h2>')
	
def fun3(request):
	return HttpResponse('<h1> Function 03 </h1>')
	
def fun4(request):
	return HttpResponse('<h1> Function 04 </h1>')
	
def fun5(request):
	return HttpResponse('<h2> Function 05 </h2>')