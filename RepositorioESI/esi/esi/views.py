from django.shortcuts import render
from apps.noticias import views
from apps.noticias.models import New
from apps.foro.models import Post as postmodel
from apps.foro.views import *




def Home(request):
	p = postmodel.objects.all().order_by('-fecha_publicacion')
	n = New.objects.all().order_by('-fecha_publicacion')
	context = {
	'noticias': n,
	'posts': p,
	}
	return render(request, 'home.html', context)

#def Noticias(request):
#	return render(request,'noticias.html')
def Foro(request):
	return render(request,'foro.html')
def Mitos(request):
	return render(request,'myv/mitos.html')
def Legal(request):
	return render(request,'legal.html')
def Post(request):
    return render(request, 'post_list.html')
#def Login(request):
#	return render(request, 'login.html')
