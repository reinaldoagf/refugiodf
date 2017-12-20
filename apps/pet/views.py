from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def indexPet(request):
	return render(request,'indexPet.html')
def createPet(request):
	return render(request,'createPet.html')