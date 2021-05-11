from django.shortcuts import render
from crudApp.models import Employee

# Create your views here.

def Display(request):
	employee = Employee.objects.all()
	return render(request, 'crudApp/display.html', {'employee' : employee})