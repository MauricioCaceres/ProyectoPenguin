import requests
from pprint import pprint
"""API_KEY = "595695c3"
URL = "http://www.omdbapi.com/?apikey="
titulo = "The Matrix"
busqueda = URL + API_KEY + "&t=" + titulo

print(busqueda)

respuesta=requests.get(busqueda)
dic_peli= respuesta.json()
pprint(dic_peli) #hasta aca para ver el contenido de la pagina
pprint(dic_peli["Year"]) #aca metes loq ue queres buscar."""

#ejercicio Fight Club, imprimir el nombre del director.
#ejercicio2: funcion que reciba como argumento el TITULO y retorne Actores.

#1

"""API_KEY = "595695c3"
URL = "http://www.omdbapi.com/?apikey="
titulo = "Fight Club"
busqueda = URL + API_KEY + "&t=" + titulo

respuesta1 = requests.get(busqueda)
dic_1 = respuesta1.json()
pprint(dic_1["Director"])"""

def BUSQUEDA(pelicula):
    API_KEY = "595695c3"
    URL = "http://www.omdbapi.com/?apikey="
    pelicula = input("Inserte nombre del film:",)
    titulo = pelicula
    busqueda = URL + API_KEY + "&t=" + titulo
    respuesta1 = requests.get(busqueda)
    dic_2 = respuesta1.json()
    pprint(dic_2["Actors"])    

BUSQUEDA("")




