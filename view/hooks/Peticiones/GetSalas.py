import requests
def GetSalas(idSala):
    res = requests.get(f"http://localhost:8080/getSalas?idSalas={idSala}")
    return res.json()
def GetAllSalas():
    res = requests.get(f"http://localhost:8080/getSalasAll")
    return res.json()