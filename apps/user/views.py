from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


from apps.user.forms import registerForm
# Create your views here.
class userCreate(CreateView):
	model= User
	template_name= 'userCreate.html'
	form_class= registerForm
# def userLogin(request):
# 	form=UserCreationForm()
# 	return render(request, 'userLogin.html',{'form':form})