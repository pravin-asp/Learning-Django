from django.shortcuts import render

# Create your views here.
'''def cookies_count_view(request):
	count = request.COOKIES.get('count', 0)
	totalCount = int(count) + 1
	response = render(request, 'cookiesApp/cookiescount.html', {'count' : totalCount})
	response.set_cookie('count', totalCount)
	return response'''
	
def cookies_count_view(request):
	count = request.session.get('count', 0)
	totalCount = int(count) + 1
	request.session['count'] = totalCount
	print(request.session.get_expiry_date())
	print(request.session.get_expiry_age())
	return render(request, 'cookiesApp/cookiescount.html', {'count' : totalCount})