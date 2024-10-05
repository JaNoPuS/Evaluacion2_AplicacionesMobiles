from django.urls import path
from . import views

urlpatterns = [
    path('tabla/', views.vistaTabla, name='vistaTabla'),
    path('loteria/', views.vistaLoteria, name='vistaLoteria'),
]