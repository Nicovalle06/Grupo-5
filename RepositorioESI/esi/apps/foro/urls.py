from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "foro"

urlpatterns = [
	path('admin/', admin.site.urls),
	path('Crear/', views.Crear.as_view(), name="crear"),
	path('Listar/', views.Listar.as_view(), name="listar"),
	


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
