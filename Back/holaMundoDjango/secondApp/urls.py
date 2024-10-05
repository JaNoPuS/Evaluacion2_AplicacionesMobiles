from django.urls import path
from secondApp.views import saludo 

urlpatterns = [
    path("", saludo)
]

