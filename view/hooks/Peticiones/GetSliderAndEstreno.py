import requests

def GetEstreno(id):
    # Realizar la solicitud GET para obtener la imagen
    response = requests.get(f"http://localhost:8080/getEstrenos?id={id}")
    return response.json()
def GetEstrenoAll():
    # Realizar la solicitud GET para obtener la imagen
    response = requests.get(f"http://localhost:8080/getEstrenosAll")
    return response.json()
def GetEstrenoPage(page, limit):
    # Realizar la solicitud GET para obtener la imagen
    response = requests.get(f"http://localhost:8080/getEstrenosPagination?page={page}&limit={limit}")
    return response.json()
