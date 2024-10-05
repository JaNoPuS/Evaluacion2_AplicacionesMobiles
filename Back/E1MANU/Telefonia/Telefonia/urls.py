from django.contrib import admin
from django.urls import path, include
from Telefonia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('serviciosApp.urls')),
    path('informacion/', include('infoApp.urls')),
    path('', views.menu),
]


