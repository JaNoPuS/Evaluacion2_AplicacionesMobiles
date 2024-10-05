from django.shortcuts import render
from django.http import HttpResponse
import datetime

def saludo(request):
    s = "<h1> Hola desde la segunda app! </h1>"
    url = "<a href='-../firstApp/ahora' > Ver Fecha y hora actual </a>"
    pagina = s + url