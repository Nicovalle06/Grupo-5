
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib import admin
from ckeditor.fields import RichTextField
from datetime import datetime
from django.utils.functional import lazy
from django.utils.timezone import localtime, now




class New(models.Model):
	titulo = models.CharField('titulo de la noticia',max_length=200)
	autor = models.CharField('autor',max_length=200)
	copete = models.TextField('copete')
	cuerpo = RichTextField('texo')
	imagen = models.URLField('imagen')
	fecha_publicacion = models.DateTimeField('fecha de la publicacion',editable=True, auto_now_add=True, auto_now=False)
	fuente = models.URLField('fuente URL',max_length=400)

	def __str__(self):
		return self.titulo
