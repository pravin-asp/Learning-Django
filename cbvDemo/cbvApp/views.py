from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from django.http import HttpResponse

class FirstView(View):
	def get(self, request):
		return HttpResponse('<h1> Hello Everyone </h1>')