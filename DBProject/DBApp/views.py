from django.shortcuts import render
from DBApp.models import Employee

#from django.http import HttpResponse
# Create your views here.

def empDetails(request):
	
	#return HttpResponse('<h1> This is DB Project </h1>')
	
	emp_data = Employee.objects.all()
	emp_dict = {'emp_list' : emp_data}
	return render(request, 'templates/DBLearning.html', context = emp_dict)