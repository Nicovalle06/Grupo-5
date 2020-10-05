#from django.contrib import admin
#from .models import Post, Tematica, Comentario

from django.contrib import admin
from .models import Post, Tematica, Comentario
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class PostResource(resources.ModelResource):
    model = Post
class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','texto','autor','fecha_publicacion']
    list_display = ('titulo','texto','fecha_publicacion','tematica',)
admin.site.register(Post,PostAdmin)

class ComentarioResource(resources.ModelResource):
    model = Comentario
class ComentarioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['usuario','post','mensaje','fecha_creacion']
    list_display = ('usuario','post','fecha_creacion','mensaje',)
admin.site.register(Comentario,ComentarioAdmin)

admin.site.register(Tematica)

# Register your models here.
#admin.site.register(Post)
#admin.site.register(Tematica)
#admin.site.register(Comentario)
