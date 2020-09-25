from django.shortcuts import render, redirect
from .forms import AltaPost , Comentarios
from .models import Post, Tematica
from django.views.generic import CreateView, DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#from django.utils import timezone

from django.core.paginator import Paginator



def listing(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list,3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'foro/listar.html', {'page_obj': page_obj})



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


#class Listar(ListView):
#    model = Post
#    template_name = 'foro/listar.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'foro/detalle.html'



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

<<<<<<< HEAD
    return render(request, 'foro/buscar.html',context )
=======
    return render(request, 'foro/listar.html', context)


def Comentario(request):
    if request.method == 'POST':
        form = Comentarios(request.POST)
    else:
        form = Comentarios()
    return render_to_response('detalle.html', {'form': form})
>>>>>>> 40ae253ca52e7cfae27d1aa6e5af01ae9e347448
