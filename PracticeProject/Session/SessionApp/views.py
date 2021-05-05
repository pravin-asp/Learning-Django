from django.shortcuts import render

# Create your views here.
def SessionCount(request):
	count = request.session.get('count', 0)
	totalCount = int(count) + 1
	request.session['count'] = totalCount
	return render(request, 'SessionApp/display.html', {'count' : totalCount})
	
def CookieCount(request):
	count = request.COOKIES.get('count', 0)
	totalCount = int(count) + 1
	response = render(request, 'SessionApp/display.html', {'count' : totalCount})
	response.set_cookie('count', totalCount)
	return response
