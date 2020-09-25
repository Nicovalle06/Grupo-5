
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib import admin
# Create your models here.



class New(models.Model): 
	titulo = models.CharField(max_length=200)
	autor = models.CharField(max_length=200)
	cuerpo = models.TextField()
	imagen = models.ImageField()
	fecha_publicacion = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.titulo