from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from django.contrib import admin




from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('home/',views.Home,name="home"),
    path('noticias/',views.Noticias,name="noticias"),
    path('foro/',views.Foro,name="foro"),
    path('foro/post_list/',views.Post,name="post_list"),
    path('mitos/',views.Mitos,name="mitos"),
    path('legal/',views.Legal,name="legal"),
   
]	


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)