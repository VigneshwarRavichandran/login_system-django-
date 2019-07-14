from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from .forms import LoginForm

def index(request):
	# user_list = User.objects.all()
	context = {
	'invalid_password' : False,
	'invalid_username' : False
	}
	if request.method == 'GET':
		return render(request, 'login_module/index.html')
	if request.method == 'POST':
		username = request.POST.get("username")
		password = request.POST.get("password")
		try:
			user = User.objects.get(username = username)
			if user.password == password:
				return HttpResponseRedirect("/login_module/welcome/")
			else:
				context['invalid_password'] = True
				return render(request, 'login_module/index.html', context)
		except:
			context['invalid_username'] = True
			return render(request, 'login_module/index.html', context)

def welcome(request):
	return render(request, 'login_module/welcome.html')

def results(request, user_id):
	return HttpResponse('Results {0}'.format(user_id))