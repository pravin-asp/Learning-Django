from django.shortcuts import render, redirect
from crudApp.models import Employee
from crudApp.forms import EmpForm
# Create your views here.

def Display(request):
	employee = Employee.objects.all()
	return render(request, 'crudApp/display.html', {'employee' : employee})
	
def AddEmp(request):
	emp = EmpForm()
	if request.method == 'POST':
		emp = EmpForm(request.POST)
		if emp.is_valid():
			emp.save()
			return redirect('/check/display/')
	return render(request, 'crudApp/form.html', {'emp' : emp})
	
def delete(request, id):
	employee = Employee.objects.get(pk = id)
	employee.delete()
	return redirect('/check/display/')
	
def update(request, id):
	emp = Employee.objects.get(pk = id)
	if request.method == 'POST':
		form = EmpForm(request.POST, instance = emp)
		if form.is_valid():
			form.save()
			return redirect('/check/display/')
	return render(request, 'crudApp/update.html', {'emp' : emp})