from django.shortcuts import render
from django.http import HttpResponse

def vistaMenu(request):
    titulo = """
  <!DOCTYPE html>
  <html lang="es">
  <head>
      <meta charset="UTF-8">
      <title>Menu Principal</title>
  </head>
  <body>
      <h1>Seleccione una opción</h1>
      <ul>
          <li><a href="/optionApp/tabla/">Vista Tabla</a></li>
          <li><a href="/optionApp/loteria/">Vista Lotería</a></li>
      </ul>
  </body>
  </html>
  """
    volver = "<br><a href='../'>Volver</a>"
    return HttpResponse(titulo)