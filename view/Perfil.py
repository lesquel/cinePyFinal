import customtkinter as ctk
from components.Text import Text
from components.Img import Img
from components.Nav import Nav

def Perfil(ventana, infoUser):
    # Crear el marco principal
    frame = ctk.CTkFrame(ventana, corner_radius=20)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Configurar grid para el marco principal
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    # Añadir el menú lateral
    Nav(frame, [
        {"ventana": ventana, "infoUser": infoUser},
    ])

    # # Añadir imagen redondeada de perfil
    img_perfil = Img(frame, url=infoUser["img"]) 
    img_perfil.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    # Añadir nombre de usuario
    Text(frame, texto=f"Usuario: {infoUser["nombre"]}", tamanio=16).grid(row=1, column=1, padx=5, pady=10)

    # Añadir contraseña
    Text(frame, texto=f"Contraseña: {infoUser['contra']}", tamanio=16).grid(row=2, column=1, padx=5, pady=10)

    return frame
