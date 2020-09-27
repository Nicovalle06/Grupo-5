from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import DetailView
from django.urls import path
from . import views

app_name = "myv"

urlpatterns = [
	path('admin/', admin.site.urls),
	path('mitos/', views.Listar_myv, name="mitos"),
    path('detalles/<int:pk>', views.Detalles_myv.as_view(), name = 'detalles'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
