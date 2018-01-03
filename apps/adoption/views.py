from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.pet.models import Request
from apps.adoption.forms import RequestForm
from django.http import HttpResponse
# from apps.adoption.forms import PersonaForm
# Create your views here.

class requestIndex(ListView):
	model= Request
	paginate_by=5
	#Probando filtrado de queryset
	#queryset= Request.objects.filter(people__name='oriana')
	#queryset= Request.objects.filter(idOfPets=2)
	template_name='requestIndex.html'
class requestCreate(CreateView):
	model= Request
	form_class= RequestForm
	template_name='requestCreate.html'
class requestUpdate(UpdateView):
	model= Request
	form_class= RequestForm
	template_name='requestUpdate.html'
class requestDelete(DeleteView):
	model= Request
	template_name='requestDelete.html'