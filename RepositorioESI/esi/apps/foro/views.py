from django.shortcuts import render
from .forms import AltaPost
from .models import Post
from django.views.generic import CreateView
from django.urls import reverse_lazy
#from django.utils import timezone

# Create your views here.

#Vista basada en funciones
#def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'foro/post_list.html', {'posts': posts})


#Vistas basadas en clases
class Crear(CreateView):
    model = Post
    form_class = AltaPost
    template_name = 'foro/crear.html'
    success_url = reverse_lazy('home')
