from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign/', include('sign.urls'), name="sign"),
    path('map/', include('mapAPI.urls'), name="mapAPI"),
    path('', views.redirectToMapMain),
]
