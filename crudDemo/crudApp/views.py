from django.shortcuts import render
from crudApp.models import Student
from crudApp.forms import StudentForm

# Create your views here.
def retrieve_view(request):
	student = Student.objects.all()
	return render(request, 'crudApp/index.html', {'student' : student})
	
def form_view(request):
	form = StudentForm()
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request, 'crudApp/create.html', {'form' : form})