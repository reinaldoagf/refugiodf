from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView
from apps.pet.models import Request
from apps.adoption.forms import RequestForm
from django.http import HttpResponse
# from apps.adoption.forms import PersonaForm
# Create your views here.

class requestIndex(ListView):
	model= Request
	template_name='requestIndex.html'
class requestCreate(CreateView):
	model= Request
	form_class= RequestForm
	template_name='requestCreate.html'