from django.shortcuts import render, redirect
from .forms import SignInForm
from .forms import LogInForm
from d06.settings import NAME
from django.contrib.auth import get_user_model
from .models import MyUser
import random
from django.contrib.auth import authenticate, login, logout
# Create your views here.

User = get_user_model()

def check_session(request):
	user_name = request.session.get('user_name', None)
	if not user_name:
		request.session.set_expiry(42)
		user_name = NAME[random.randrange(10)]
		request.session['user_name'] = user_name
	return user_name

def index(request):
	if request.user.is_authenticated:
		user_name = request.user.username
	else:
		user_name = check_session(request)
	return render(request, 'index.html', {'user_name': user_name})

def get_all(request):
	users = MyUser.objects.all()
	return render(request, 'all.html', {'users': users})

# def log_in(request):
# 	user_name = check_session(request)
# 	if request.method == "POST":
# 		form = LogInForm(request.POST)
# 		if form.is_valid():
#
# 	else:
# 		form = LogInForm()
# 	return render(request, 'log_in.html', {'user_name': user_name, 'form': form})

def sign_in(request):
	if request.user.is_authenticated:
		return redirect("/")
	else:
		user_name = check_session(request)
	if request.method == "POST":
		form = SignInForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			pwd = form.cleaned_data['password']
			user = User.objects.create_user(username=name, password=pwd)
			login(request, user)
			return redirect('/')
	else:
		form = SignInForm()
	return render(request, 'sign_in.html', {'user_name': user_name, 'form': form})
