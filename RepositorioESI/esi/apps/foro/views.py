from django.shortcuts import render, redirect
from .forms import AltaPost
from .models import Post, Tematica
from django.views.generic import CreateView, DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#from django.utils import timezone

#Vistas basadas en clases
class Crear(LoginRequiredMixin,CreateView):
    model = Post
    form_class = AltaPost
    template_name = 'foro/crear.html'
    success_url = reverse_lazy('foro:listar')
    def form_valid(self, form):
        p = form.save(commit = False)
        p.autor = self.request.user
        p.save()
        return redirect(self.success_url)


class Listar(ListView):
    model = Post
    template_name = 'foro/listar.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'foro/detalle.html'


def Buscar(request):
    context = {}
    tematicas = Tematica.objects.all()
    context['tematica'] = tematicas
    return render(request, 'foro/buscar.html', context)
