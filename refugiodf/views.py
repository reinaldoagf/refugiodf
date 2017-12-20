from django.shortcuts import render

def index(request):
	return render(request,'base/base.html')
#busca luego manera de arreglar esto