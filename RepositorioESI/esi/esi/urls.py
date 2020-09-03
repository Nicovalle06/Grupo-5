
from django.contrib import admin
from django.urls import path


from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('home/',views.Home,name="home"),
]
