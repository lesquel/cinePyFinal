import requests 
def GetUser(usuario, contrasena):
    res = requests.get(f"http://localhost:8080/getUsuario?nombre={usuario}&contra={contrasena}")
    json = res.json()
    return json
def GetUserId(idUsuario):
    res = requests.get(f"http://localhost:8080/getUsuarioId?id={idUsuario}")
    json = res.json()
    return json
