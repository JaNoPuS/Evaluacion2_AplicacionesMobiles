from django.shortcuts import render
from django.http import HttpResponse

def servicios(request):
    titulo = "<h1>Nuestros Servicios</h1>"
    info = "<p>Aquí van los servicios</p>"
    volver = "<br><a href='../'>Volver</a>"
    pagina = titulo + info + volver
    return HttpResponse(pagina)

def precios(request):
    titulo = "<h1>Precios</h1>"
    info = "<p>Aquí van precios</p>"
    volver = "<br><a href='../../'>Volver</a>"
    pagina = titulo + info + volver
    return HttpResponse(pagina)