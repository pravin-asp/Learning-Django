from django.shortcuts import render

# Create your views here.
def Session(request):
	count = request.session.get('count', 0)
	totalCount = int(count) + 1
	request.session['count'] = totalCount
	print(request.session.get_expiry_date())
	print(request.session.get_expiry_age())
	return render(request, 'CombineApp/display1.html', {'count' : totalCount})