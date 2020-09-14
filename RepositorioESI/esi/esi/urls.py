from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth
from django.contrib import admin

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('noticias/',views.Noticias,name="noticias"),
    path('mitos/',views.Mitos,name="mitos"),
    path('legal/',views.Legal,name="legal"),
    path('Login',auth.LoginView.as_view(template_name  = "usuarios/login.html"), name="login"),
    path('Logout',auth.LogoutView.as_view(), name="logout"),


    path('foro/',include('apps.foro.urls')),
    path('usuarios/',include('apps.usuarios.urls'))
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
