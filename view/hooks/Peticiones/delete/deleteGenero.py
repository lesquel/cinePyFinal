import requests
def deleteGenero(id, main_frame, infoUser, ventana):
    # Aquí puedes agregar la lógica para eliminar el género
    url = f"http://localhost:8080/deleteGenero?id={id}"
    response = requests.get(url)
    from components.tablaCrud.tablaGenero import TablaGenero
    TablaGenero(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    return response.json()