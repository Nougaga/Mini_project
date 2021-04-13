from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirectToMain),
    path('main/',views.main_test),
    path('path_search/', views.path_search),
]
