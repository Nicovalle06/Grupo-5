from django.shortcuts import render


def Home(request):
	return render(request,'home.html')
def Noticias(request):
	return render(request,'noticias.html')
def Foro(request):
	return render(request,'foro.html')
