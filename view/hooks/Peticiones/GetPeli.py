import requests
from hooks.ModelRequest import ModelRequest

def GetAllPeli(page, limit=5):
    def peticion(page, limit):
        res = requests.get(f"http://localhost:8080/getPeliculas?page={page}&limit={limit}")
        return res.json()
    return ModelRequest(peticion, page, limit)

def GetPeliId(idPelicula):
    def peticion(idPelicula):
        res = requests.get(f"http://localhost:8080/getPeliculaId?id={idPelicula}")
        infoPelicula = res.json()
        return infoPelicula
    return ModelRequest(peticion, idPelicula)

def GetPeliTodasAll():
    def peticion():
        res = requests.get(f"http://localhost:8080/getPeliculasAll")
        return res.json()
    return ModelRequest(peticion)

def GetPeliByNombre(nombre):
    def peticion(nombre):
        res = requests.get(f"http://localhost:8080/getPeliculasByNombre?nombre={nombre}")
        return res.json()
    return ModelRequest(peticion, nombre)
def GetPeliByGenero(idGenero):
    def peticion(idGenero):
        res = requests.get(f"http://localhost:8080/getPeliculasByGenero?id={idGenero}")
        return res.json()
    return ModelRequest(peticion, idGenero)
