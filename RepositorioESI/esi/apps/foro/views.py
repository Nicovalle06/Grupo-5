from django.shortcuts import render, redirect
from .forms import AltaPost
from .models import Post
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#from django.utils import timezone

# Create your views here.

#Vista basada en funciones
#def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'foro/post_list.html', {'posts': posts})


#Vistas basadas en clases
class Crear(LoginRequiredMixin,CreateView):
    model = Post
    form_class = AltaPost
    template_name = 'foro/crear.html'
    success_url = reverse_lazy('foro:listar')
    def form_valid(self,form):
    	p = form.save(commit=False)
    	p.autor = self.request.user
    	p.save()
    	return redirect(self.success_url)


class Listar(ListView):
    model = Post
    template_name = 'foro/listar.html'

class Mostrar(DetailView):
    template_name = 'foro/detalle.html'
    model = Post    
