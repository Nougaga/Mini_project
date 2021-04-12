from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign/', include('sign.urls'), name="sign"),
    path('map/', include('mapAPI.urls'), name="mapAPI"),
]
