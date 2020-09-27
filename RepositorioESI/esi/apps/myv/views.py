from django.shortcuts import render
from .models import Verdad
from django.views.generic.list import ListView
from django.views.generic import DetailView


# Create your views here.
class Mitos(ListView):
	model = Verdad
	template_name = 'myv/mitos.html'

def Listar_myv(request):
    context = {}
    myv = Verdad.objects.all()
    context['myv'] = myv
    return render(request, 'myv/mitos.html', context)

class Detalles_myv(DetailView):
    model = Verdad
    template_name = 'myv/detalles.html'