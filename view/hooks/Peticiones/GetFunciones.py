import requests
import json
def GetFuncionesIdDePelicula(idPelicula):
    resques = requests.get(f"http://localhost:8080/getFunciones?idPelicula={idPelicula}")
    resques = resques.json()
    if not resques:
        return []
    for i, v in enumerate(resques):
        resques[i]["sillas"] = json.loads(resques[i]["sillas"])

    return resques
def getAllFunciones():
    resques = requests.get(f"http://localhost:8080/getFuncionesAll")
    resques = resques.json()
    for i, v in enumerate(resques):
        resques[i]["sillas"] = json.loads(resques[i]["sillas"])

    return resques