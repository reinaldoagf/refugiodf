from django.shortcuts import render,redirect
from apps.pet.forms import PetForm
from apps.pet.models import Pet
# Create your views here.
def petIndex(request):
	pet=Pet.objects.all().order_by('id')
	context={'pets':pet}
	return render(request, 'petIndex.html',context)
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