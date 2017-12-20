from django.shortcuts import render,redirect
from django.http import HttpResponse
# from apps.adoption.forms import PersonaForm
# Create your views here.

def indexRequest(request):
	return render(request,'base/base.html')
def createRequest(request):
	return HttpResponse('createRequest')
	# if request.method== 'POST':
	# 	form=PersonaForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 	return redirect('persona_index')
	# else:
	# 	form=PersonaForm()
	# return render(request,'persona_create.html',{'form':form})