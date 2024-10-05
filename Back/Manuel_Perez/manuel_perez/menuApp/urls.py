from django.urls import path, include
from menuApp import views

urlpatterns = [
    path('', views.vistaMenu), ]
