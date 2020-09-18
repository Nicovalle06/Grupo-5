from django.shortcuts import render
from .models import New
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
# Create your views here.

class Noticia(ListView):
	model = New
	template_name = 'noticias.html'
	