import requests
def insertSala(nombre, fillas, columnas, ventana, infoUser, main_frame):
    # http://localhost:8080/introSala?nombre=1&fillas=1&columnas=1
    url = f"http://localhost:8080/introSala?nombre={nombre}&fillas={fillas}&columnas={columnas}"
    response = requests.get(url)
    from components.tablaCrud.tablaSalas import TablaSala
    TablaSala(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    return response.json()