import bs4
import requests

resultado = requests.get(url="https://www.escueladirecta.com/l/products?sortKey=name&sortDirection=asc&page=1")

sopa = bs4.BeautifulSoup(resultado.text, "lxml")


imagenes = sopa.select(".ProductImage")
num_imagen = 0
for imagen in imagenes:
    print(imagen["src"])
    obtener_imagen = requests.get(imagen["src"])
    num_imagen += 1
    nom_img = "imagen"+ str(num_imagen) +".jpg"
    ruta = './img/' + nom_img
    file = open(ruta, "wb")
    file.write(obtener_imagen.content)
    file.close()
