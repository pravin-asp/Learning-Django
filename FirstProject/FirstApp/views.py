from django.shortcuts import render
from django.http import HttpResponse

def wish(request):
	#message = '<h1>Hi Buddy, How are you?</h1>'
	message = """<h1>Hi Welcome to my Webpage</h1><br>
			<p>Please login to read more</p>
			<table><tr><td>User Name<td><td><input type = "text"><td><tr>
			<tr><td>Password<td><td><input type = "text"><td><tr>
			</table>
			"""
	return HttpResponse(message)
# Create your views here.

# http://127.0.0.1:8000/wish --> HTTP Request

# HTTP Response

'''
message = """
			<h1>Hi Welcome to my Webpage</h1><br>
			<p>Please login to read more</p>
			<table><tr><td>User Name<td><td><input type = "text"><td>tr>
			<tr><td>Password<td><td><input type = "text"><td><tr>
			</table>
			"""
'''