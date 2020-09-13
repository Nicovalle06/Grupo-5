from django.db import models
from django.utils import timezone
#from django.template.defaultfilters import slugify

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    mail = models.EmailField()

    def __str__(self):
        return self.nombre


class Post(models.Model):
    autor = models.CharField(max_length = 50)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    usuario = models.ForeignKey(Usuario, related_name = 'miUsuario', null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.titulo
