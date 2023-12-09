"""
URL configuration for redsocial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from apps.usuarios import views as viewsUser
from apps.publicaciones import views


urlpatterns = [
    path('login/', viewsUser.user_login),
    path('usuarios/', viewsUser.usuario_list),
    path('usuario/', viewsUser.get_user_by_email),
    path('publicacion/', views.publicacion_list),
    path('publicacion/<int:pk>/', views.publicacion_detail),
    path('publicacionComentario/', views.publicacionComentario_list),
    path('publicacionComentario/<int:pk>/', views.publicacionComentario_detail),
    path('publicacionFile/', views.publicacionFile_list),
    path('publicacionFile/<int:pk>/', views.publicacionFile_detail),
    path('publicacionReaccion/', views.publicacionReaccion_list),
    path('publicacionReaccion/<int:pk>/', views.publicacionReaccion_detail),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
