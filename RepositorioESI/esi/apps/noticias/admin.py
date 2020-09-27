from django.contrib import admin
from .models import New
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class NewResource(resources.ModelResource):
    model = New
        


class NewAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','autor','cuerpo','copete']
    list_display = ('titulo','autor','fecha_publicacion','imagen',)


admin.site.register(New,NewAdmin)