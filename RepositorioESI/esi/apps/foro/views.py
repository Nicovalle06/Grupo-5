from django.shortcuts import render, redirect, get_object_or_404
from .forms import AltaPost , CommentForm
from .models import Post, Tematica
from django.views.generic import CreateView, DetailView
#from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse,Http404
from apps.foro.models import Post, Comentario
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

import json





#--------------Vista basada en clases-----------------
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



#class Listar(ListView):
#    model = Post
#    template_name = 'foro/listar.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'foro/detalle.html'


#------------------Funciones-------------------

def listing(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter()
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(texto__icontains = queryset)

        ).distinct()

    paginator = Paginator(posts,3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'foro/listar.html', {'posts': posts})



def buscar(request):
    context = {}
    tematicas = Tematica.objects.all()
    context['tematica'] = tematicas
    id_tem = request.GET.get('buscar', None)

    if id_tem:
        resultado = Post.objects.filter(tematica = id_tem).order_by('-fecha_publicacion')
        context['posteos'] = resultado

    else:
        todos = Post.objects.all().order_by('-fecha_publicacion')
        context['posteos'] = todos

    return render(request, 'foro/buscar.html',context )

@login_required
def agregar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comentario = form.save(commit=False)
            Comentario.usuario = request.user
            Comentario.post = post
            Comentario.save()
            return redirect('foro:detalle', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'foro/agregarcomentario.html', {'form': form})
