from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def WelcomePage(response):
	"""message = '''<h1>Welcome to my Practice Project Page</h1>
				<h4>This is for my reference Django Project</h4>
				<p>This project is only for my practice. This helps me to understan 
				the Django project. How it works? These are my learnings. Thank YOu !!!</p>'''
	return HttpResponse(message)"""
	return render(response, 'Templates/practice.html')