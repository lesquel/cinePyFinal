import requests
def getGenero(idGenero):
    res = requests.get(f"http://localhost:8080/getGenero?id={idGenero}")
    json = res.json()
    return json
def getAllGeneros():
    res = requests.get(f"http://localhost:8080/getAllGenero")
    json = res.json()
    return json