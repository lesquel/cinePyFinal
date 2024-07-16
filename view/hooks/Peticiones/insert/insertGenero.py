import requests
def insertGenero(nombre, ventana, infoUser):
    # Aquí puedes agregar la lógica para agregar el género
    url = f"http://localhost:8080/introGenero?nombre={nombre}"
    response = requests.get(url)
    from TablaCrudPelicula import TablaCrudPelicula
    TablaCrudPelicula(ventana=ventana, infoUser=infoUser)
    return response.json()