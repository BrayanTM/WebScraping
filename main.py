import bs4
import requests

# Definir la URL base del sitio web a scrapear
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista de titulos con 4 o 5 estrellas
titulos = []

# Iterar a través de las páginas del sitio web
for pagina in range(1, 51):

    # Crear sopa para cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url=url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # Seleccionar todos los libros en la página
    libros = sopa.select('.product_pod')

    # Iterar a través de los libros y filtrar por calificación
    for libro in libros:

        # Obtener la calificación del libro
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # Obtener el título del libro
            titulo = libro.select('a')[1]['title']
            titulos.append(titulo)

# Imprimir los títulos de los libros con 4 o 5 estrellas
for titulo in titulos:
    archivo = open("titulos.txt", "a", encoding="utf-8")
    archivo.write(titulo + "\n")
    archivo.close()