from django.shortcuts import render
from DjanogApp.models import Login
# Create your views here.
def LoginInfo(request):
	info = Login.objects.all()
	return render(request, 'DjangoApp/info.html', {'info' : info})