import requests
import json
def cerateSillas(filas, columnas):
    sillas = []
    for i in range(filas):
        sillas.append(['L'] * columnas)
    return sillas

def insertFuncion(fecha, idSala, idPeliculas, ventana, infoUser, main_frame):
    # Crear la lista de sillas
    from hooks.Peticiones.GetSalas import GetSalas
    infoSala = GetSalas(idSala=idSala)
    sillas = cerateSillas(filas=infoSala["fillas"], columnas=infoSala["columnas"])
    sillas = json.dumps(sillas)
    url = f"http://localhost:8080/introFunciones?fecha={fecha}&idSala={idSala}&idPeliculas={idPeliculas}&sillas={sillas}"
    res = requests.get(url)
    from components.tablaCrud.tablaFunciones import TablaFunciones
    TablaFunciones(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    return res.json()