import json
from rest_framework.views import APIView

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from apps.pet.models import Request

from apps.adoption.serializers import PeopleSerializer
from apps.adoption.models import People
from apps.adoption.forms import RequestForm

# from apps.adoption.forms import PersonaForm
# Create your views here.
class requestIndex(ListView):
	model= Request
	paginate_by=4
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
class PeopleAPI(APIView):
	serializer= PeopleSerializer
	def get(self, request, format=None):
		peopleList=People.objects.all()
		response= self.serializer(peopleList,many=True)
		return HttpResponse(json.dumps(response.data),content_type='application/json')
