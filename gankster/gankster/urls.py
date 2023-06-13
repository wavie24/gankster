from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('komoditas/', include('komoditas.urls')),
    path('simulasi/', include('simulasi.urls')),
]
