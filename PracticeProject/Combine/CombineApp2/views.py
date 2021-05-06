from django.shortcuts import render

# Create your views here.
def Cookies(request):
	count = request.COOKIES.get('count', 0)
	totalCount = int(count) + 1
	response = render(request, 'CombineApp/display2.html', {'count' : totalCount})
	response.set_cookie('count', totalCount)
	return response