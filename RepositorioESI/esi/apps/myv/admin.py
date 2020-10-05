#from django.contrib import admin
#from .models import Verdad

from django.contrib import admin
from .models import Verdad
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class VerdadResource(resources.ModelResource):
    model = Verdad
class VerdadAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['title','tematicas','description','conclusion']
    list_display = ('title','tematicas','description','created_date',)
admin.site.register(Verdad,VerdadAdmin)

# Register your models here.
#admin.site.register(Verdad)
