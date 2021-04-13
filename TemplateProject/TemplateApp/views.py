from django.shortcuts import render
import datetime
# Create your views here.

def display(request):
	message = 'Hi'
	date = datetime.datetime.now()
	hour = int(date.strftime('%H'))
	if hour < 12:
		message += ' Good Morning'
	else:
		message += ' Good Evening'
	date_dict = {'display_date' : date, 'name' : 'Pravin A S', 'message' : message}
	return render(request, 'TemplateApp/abc.html', context = date_dict)