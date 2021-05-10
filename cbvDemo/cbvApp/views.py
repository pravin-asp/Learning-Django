from django.shortcuts import render
from django.views.generic import View, TemplateView
# Create your views here.
from django.http import HttpResponse

class FirstView(View):
	def get(self, request):
		return HttpResponse('<h1> Hello Everyone </h1>')
		
class SecondView(TemplateView):
	def get(self, request):
		template_view = 'cbvApp/base.html'
		return render(request, template_view)