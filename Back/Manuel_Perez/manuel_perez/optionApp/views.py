from django.shortcuts import render
from django.http import HttpResponse
import random


def vistaTabla(request):
  vistaTabla = """
      <title>Mis Países Favoritos</title>
      <h1>Mis Países Favoritos</h1>
      <table border="1">
          <thead>
              <tr>
                  <th>País</th>
                  <th>Continente</th>
                  <th>Bandera</th>
              </tr>
          </thead>
          <tbody>
              <tr>
                  <td>España</td>
                  <td>Europa</td>
                  <td><img src="https://banderasysoportes.com/xen_media/banner-full-2.jpg" alt="Bandera de España"></td>
              </tr>
              <tr>
                  <td>Brasil</td>
                  <td>América del Sur</td>
                  <td><img src="https://www.meriggi.cl/23331-large_default/bandera-brasil-est-60x90.jpg" alt="Bandera de Brasil"></td>
              </tr>
              <tr>
                  <td>Japón</td>
                  <td>Asia</td>
                  <td><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWpE0z15hxXexpKqKJ7iXt-N2K1EmtBWKrpA&s" alt="Bandera de Japón"></td>
              </tr>
          </tbody>
      <br>
      <button onclick="window.location.href='/'">Volver a la página principal</button>
  """
  return HttpResponse(vistaTabla)

def vistaLoteria(request):
  numeros = sorted(random.sample(range(1, 101), 10))
  numeros_html = ''.join(f'<li>{numero}</li>' for numero in numeros)
  vistaLoteria = f"""
  <head>
      <meta charset="UTF-8">
      <title>Números de la Suerte</title>
  </head>
  <body>
      <h1>Estos son los números de la suerte en este momento</h1>
      <ul>
          {numeros_html}
      </ul>
      <br>
      <button onclick="window.location.href='/'">Volver a la página principal</button>
  </body>
  </html>
  """
  return HttpResponse(vistaLoteria)