from django.shortcuts import render


def Home(request):
	return render(request,'home.html')
def Noticias(request):
	return render(request,'noticias.html')
def Foro(request):
	return render(request,'foro.html')
def Mitos(request):
	return render(request,'myv/mitos.html')
def Legal(request):
	return render(request,'legal.html')
def Post(request):
    return render(request, 'post_list.html')
def Login(request):
	return render(request, 'login.html')
