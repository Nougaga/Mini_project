"""mini_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

app_name = "sign"
urlpatterns = [
    path('join/', views.join, name="join"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('modi_info/', views.modi_info, name="modi_info"),
    path('user_drop/', views.user_drop, name="user_drop"),
    path('user_info/', views.user_info, name="user_info"),
    path('id_check/', views.id_check, name="id_check"),
    path('pw_check/', views.pw_check, name="pw_check"),
]
