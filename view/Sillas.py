import customtkinter as ctk
from layout import Layout
import json
from components.AllSIllas import AllSIllas
from hooks.Reserva import Reservar
from hooks.Recomendado import Recomendado

def Sillas(ventana, fun, info, idUsuario):
    # Crear el contenedor principal
    frame_principal = Layout(ventana=ventana)

    
    # Crear frame1 y frame2
    frame1 = ctk.CTkFrame(frame_principal)
    frame2 = ctk.CTkFrame(frame_principal)

    frame2.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)
    frame1.grid(row=0, column=1, sticky="nsew", padx=40, pady=40)
    
    # Cargar la matriz de sillas desde JSON
    global matriz
    matriz = fun["sillas"]

    # Lista de leyenda de sillas
    lista = [["L", "Libre", "#8888ff"], ["O", "Ocupado", "#ff8888"], ["S", "Sección|Reservado", "#888888"], ["R", "Recomendado", "#88ff88"], ["M", "Mis Sillas", "#ffff00"]]

    # Configuración de la leyenda de sillas en frame1 usando grid
    for i, v in enumerate(lista):
        label = ctk.CTkLabel(frame1, text=f"{v[0]}={v[1]}", font=("Arial", 14), bg_color=v[2])
        label.grid(row=i, column=0, sticky="w", padx=10, pady=5)
    
    # Mostrar todas las sillas en frame2
    AllSIllas(matriz=matriz, frame=frame2, idUsuario=idUsuario)
    
    # Botón para reservar en frame1
    reservar_boton = ctk.CTkButton(frame1, text="Reservar", command=lambda: Reservar(frame_principal, info, fun["id"], matriz, idUsuario))
    reservar_boton.grid(row=len(lista), column=0, sticky="ew", padx=10, pady=5)

    # Función para ejecutar el algoritmo de recomendación de asientos
    def ejecutar(idUsuario=idUsuario):
        global matriz
        matriz = Recomendado(matriz=matriz)
        AllSIllas(matriz=matriz, frame=frame2, idUsuario=idUsuario)

    # Botón para encontrar el mejor asiento en frame1
    mejor_asiento_boton = ctk.CTkButton(frame1, text="El mejor asiento", command=lambda: ejecutar(idUsuario=idUsuario))
    mejor_asiento_boton.grid(row=len(lista) + 1, column=0, sticky="ew", padx=10, pady=5)

    # Etiqueta para la pantalla en frame2
    pantalla = ctk.CTkLabel(frame2, text="Pantalla", font=("Arial", 14), bg_color="#222222", text_color="#ffffff", height=1, width=20)
    pantalla.grid(row=len(matriz) + 1, column=0, columnspan=6, padx=10, pady=10)

    from components.Regresar import RegresarFunc
    from Salas import Salas
    RegresarFunc(frame1=frame_principal, funFramereegre=lambda: Salas(ventana=ventana, infoPelicula=info, idUsuario=idUsuario))
    
    return frame_principal
