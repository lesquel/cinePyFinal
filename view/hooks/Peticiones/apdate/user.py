import requests
def update_user(id, nombre, contra, img, name, correo, edad, ventana):
    url = f"http://localhost:8080/updateUsuario?id={id}&nombre={nombre}&contra={contra}&img={img}&name={name}&correo={correo}&edad={edad}"
    response = requests.get(url)
    a = response.json()
    from tkinter import messagebox
    messagebox.showinfo("Actualización exitosa", "Tus datos han sido actualizados con éxito.")
    from Perfil import Perfil
    from hooks.Peticiones.GetUser import GetUserId
    user = GetUserId(idUsuario=id)
    Perfil(ventana=ventana, infoUser=user)
    return