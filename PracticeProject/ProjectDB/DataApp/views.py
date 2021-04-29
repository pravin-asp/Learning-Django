from django.shortcuts import render
from DataApp.models import EmployeeDetails

# Create your views here.

def EmployeeData(response):
	detail = EmployeeDetails.objects.all()
	dict = {'Data' : detail}
	return render(response, 'template/display.html', context = dict)