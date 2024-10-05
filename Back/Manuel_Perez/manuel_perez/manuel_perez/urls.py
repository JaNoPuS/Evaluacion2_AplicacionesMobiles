from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menuApp.urls')),  # Página principal
    path('optionApp/', include('optionApp.urls')),  # URLs de optionApp
]