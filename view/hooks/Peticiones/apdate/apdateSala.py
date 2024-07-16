import requests
def apdateSala(id, nombre, fillas, columnas, ventana, infoUser, ventanaHelp, main_frame):
    # http://localhost:8080/updateSala?id=1&nombre=1&fillas=1&columnas=1
    ventanaHelp.destroy()
    url = f"http://localhost:8080/updateSala?id={id}&nombre={nombre}&fillas={fillas}&columnas={columnas}"
    requests.get(url)
    from components.tablaCrud.tablaSalas import TablaSala
    TablaSala(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    return