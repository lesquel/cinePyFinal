import requests
def insertUser(nombre, img, edad, usuario, correo, contrasena):
    # Realizar la solicitud POST para insertar un nuevo usuario

    url = f"http://localhost:8080/introUsuario?nombre={nombre}&contra={contrasena}&img={img}&name={usuario}&correo={correo}&edad={edad}"
    print(url)
    response = requests.post(url)
    if response.status_code == 200:
        # Devolver la respuesta en formato JSON
        return response.json()
    else:
        # Manejar el caso de error en la respuesta
        print(f"Error: {response.status_code} - {response.text}")
        return None 