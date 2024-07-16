import customtkinter as ctk
from layout import Layout

from components.index.pelicuas import Pelicuas
def Index(ventana, infoUser, ifAdmin=False):
    # Crear el marco principal
    frame = Layout(ventana)
    # Crear el menú lateral
    if ifAdmin:
        from components.Nav import NavAdmid
        NavAdmid(frame, [
            {"ventana": ventana, "infoUser": infoUser},
        ])
    else:
        from components.Nav import Nav
        Nav(frame, [
            {"ventana": ventana, "infoUser": infoUser},
        ])

    # Crear un marco scrollable para el contenido principal
    scrollable_frame = ctk.CTkFrame(frame)
    scrollable_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # Añadir título al scrollable_frame
    ctk.CTkLabel(scrollable_frame, text="Películas", font=("Arial", 24), corner_radius=20).grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    Pelicuas(scrollable_frame, infoUser, frame, ventana, ifAdmin)
    
    return frame
