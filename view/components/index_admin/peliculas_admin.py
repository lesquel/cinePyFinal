from components.Text import Text
from components.Button import Button
from components.Img import Img
import customtkinter as ctk
from Salas import Salas
def Pelicuas(parent, infoUser, frame, ventana, ifAdmin=False):
    def Ventana(infoPelicula, idUsuario):
        from index import Index
        # Mostrar la sala de la película seleccionada
        frame2 = Salas(ventana=ventana, infoPelicula=infoPelicula, idUsuario=idUsuario)
        frame.destroy()
        frame2.grid(row=0, column=0, sticky="nsew")
        
    # Obtener la lista de películas
    from datos.peliculas import peliculas
    fila = 1
    columna = 0
    # Iterar sobre las películas para crear widgets de visualización
    for pelicula in peliculas:
        # Crear un marco para la película
        marco_pelicula = ctk.CTkFrame(parent, corner_radius=10, border_width=2)
        marco_pelicula.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

        # Mostrar la imagen de la película
        Img(marco_pelicula, pelicula["img"])

        # Crear un marco para el nombre de la película
        marco_nombre = ctk.CTkFrame(marco_pelicula)
        marco_nombre.grid(pady=(0, 10))

        # Mostrar el nombre y duración de la película
        Text(marco_nombre, texto=pelicula["nombre"], tamanio=16, row=0, column=0, padx=10, pady=10).grid(sticky="w")
        Text(marco_nombre, texto=f"Duración: {pelicula['dura']}H", tamanio=16, row=1, column=0, padx=10, pady=10).grid(sticky="w")

        if ifAdmin:
            # Crear un botón para ver más detalles de la película
            Button(marco_pelicula, texto="Editar", tamanio=16, row=2, column=0, eventoClick=lambda infoPelicula=pelicula, idUsuario=infoUser["id"]: Ventana(infoPelicula, idUsuario))
        else:
            # Crear un botón para ver más detalles de la película
            Button(marco_pelicula, texto="Ver", tamanio=16, row=2, column=0, eventoClick=lambda infoPelicula=pelicula, idUsuario=infoUser["id"]: Ventana(infoPelicula, idUsuario))

        # Actualizar las posiciones de fila y columna
        columna += 1
        if columna >= 4:
            columna = 0
            fila += 1