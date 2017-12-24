from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from apps.user.forms import registerForm
# Create your views here.
class userCreate(CreateView):
	model= User
	template_name= 'userCreate.html'
	form_class= registerForm
		