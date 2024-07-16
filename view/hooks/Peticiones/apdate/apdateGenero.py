import requests
def apdateGenero(id, nombre, ventana, infoUser, ventanaHelp):
    ventanaHelp.destroy()
    # Aquí puedes agregar la lógica para actualizar el género
    url = f"http://localhost:8080/updateGenero?id={id}&nombre={nombre}"
    response = requests.get(url)
    from TablaCrudPelicula import TablaCrudPelicula
    TablaCrudPelicula(ventana=ventana, infoUser=infoUser)
    return response.json()