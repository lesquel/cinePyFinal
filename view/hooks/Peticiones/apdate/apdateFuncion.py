import requests
import json
def apdateFuncion(id, fecha, idSala, idPeliculas, ventana, infoUser, ventanaHelp, main_frame):
    ventanaHelp.destroy()
    # http://localhost:8080/updateFunciones?id=1&idSala=1&idPeliculas=1&fecha=1
    url = f"http://localhost:8080/updateFunciones?id={id}&idSala={idSala}&idPeliculas={idPeliculas}&fecha={fecha}"
    res = requests.get(url)
    from components.tablaCrud.tablaFunciones import TablaFunciones
    TablaFunciones(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    return res.json() 