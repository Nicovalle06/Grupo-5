from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titulo
