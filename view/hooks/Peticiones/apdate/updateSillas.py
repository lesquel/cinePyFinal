import requests
import json
def updateSillas(id, sillas, idUsuario):
    # Convertir la lista de listas a una cadena JSON
    for f, v in enumerate(sillas):
        for c, v2 in enumerate(v):
            if v2 == 'R':
                sillas[f][c] = 'L'
            elif v2 == 'S':
                sillas[f][c] = idUsuario

    sillas_json = json.dumps(sillas)
    res = requests.post(f"http://localhost:8080/UpdateSillas?id={id}&sillas={sillas_json}")

    