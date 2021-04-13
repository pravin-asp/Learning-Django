from django.shortcuts import render
import datetime
# Create your views here.

def display(request):
	date = datetime.datetime.now()
	date_dict = {'display_date' : date}
	return render(request, 'TemplateApp/abc.html', context = date_dict)