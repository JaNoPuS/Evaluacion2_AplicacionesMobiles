from django.shortcuts import render
from django.http import HttpResponse

def menu(request):
    titulo = "<h1>Menu</h1>"
    logo = "<img src='https://64.media.tumblr.com/764b5685363ea76e429ef04c0cb51800/tumblr_p6btd66pBB1snnpu4o1_640.pnj' width=200 heigth=100 />"
    links = '''
    <ul>
        <li><a href="informacion">Información</a></li>
        <li><a href="servicios">Servicios</a></li>
        <li><a href="servicios/precios">Precios</a></li>
    </ul>
    '''
    pagina = titulo + logo + links
    return HttpResponse(pagina)