from django.shortcuts import render
from .models import New
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from datetime import datetime
# Create your views here.

class Noticia(ListView):
	model = New
	template_name = 'noticias.html'

def ListarNoticias(request):
    context = {}
    noticias = New.objects.all()
    context['noticias'] = noticias
    return render(request, 'noticias/nota.html', context)

class NewDetail(DetailView):
    model = New
    template_name = 'noticias/detalles.html'
"""class formarteo(request,obj):

    return "<h1> {0}</h1>".format(obj.strftime("%d %m %Y"))"""