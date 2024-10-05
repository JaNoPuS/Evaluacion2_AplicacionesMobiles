from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display(request):
    return HttpResponse("<h1> Hola Mundo </h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s= "<b> Fecha y Hora Actual: </b>" + str(dt)
    return HttpResponse(s)


