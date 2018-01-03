from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core import serializers
from apps.pet.forms import PetForm
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from apps.pet.models import Pet
# Create your views here.
def listView(request):
	petList=serializers.serialize('json',Pet.objects.all())
	return HttpResponse(petList, content_type='application/json')
def petIndex(request):
	pet=Pet.objects.all().order_by('id')
	paginator=Paginator(pet, 2)
	page = request.GET.get('page')
	try:
		pets = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		pets = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		pets = paginator.page(paginator.num_pages)
	return render(request, 'petIndex.html', {'pets': pets})
	# return HttpResponse(pagPets.object_list,content_type='application/json')
def Paginador(request, modelo, paginas):
	result_list = Paginator(modelo, paginas)
	try:
		page = int(request.GET.get('page')); #Tomamos el valor de parametro page, usando GET
	except:
		page = 1
	if (page < result_list.page(page)):
		pagina = result_list.page(page)
		Contexto = {'modelo': pagina.object_list, #Asignamos registros de la pagina
			 'page': page, #Pagina Actual
			 'pages': result_list.num_pages, #Cantidad de Paginas
			 'has_next': pagina.has_next(), #True si hay proxima pagina
			 'has_prev': pagina.has_previous(), #true si hay Pagina anterior
			 'next_page': page+1, #Proxima pagina
			 'prev_page': page-1, #Pagina Anterior
			 }
		return Contexto
def petCreate(request):
	if request.method== 'POST':
		form=PetForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('pet:petIndex')
	else:
		form=PetForm()
	return render(request, 'petCreate.html',{'form':form})
def petUpdate(request,id):
	pet=Pet.objects.get(id=id)
	if request.method=='GET' :
		form=PetForm(instance=pet)
	else:
		form=PetForm(request.POST,instance=pet)
		if form.is_valid():
			form.save()
		return redirect('pet:petIndex')
	return render(request,'petUpdate.html',{'form':form})
def petDelete(request,id):
	pet=Pet.objects.get(id=id)
	if request.method=='POST' :
		pet.delete()
		return redirect('pet:petIndex')
	return render(request,'petDelete.html',{'pet':pet})