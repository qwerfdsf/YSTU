
from django.contrib import admin
from django.urls import path, include
from mainapp.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/', include('mainapp.api.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
