from django.contrib import admin
from .models import Post, Tematica, Comentario


# Register your models here.
admin.site.register(Post)
admin.site.register(Tematica)
admin.site.register(Comentario)