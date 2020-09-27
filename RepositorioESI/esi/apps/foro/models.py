from django.db import models
from django.utils import timezone
from django.conf import settings

class Tematica(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre



class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    tematica = models.ForeignKey(Tematica, related_name='miTematica', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey('foro.Post', on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.mensaje
