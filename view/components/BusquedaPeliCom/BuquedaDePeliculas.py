import customtkinter as ctk
from components.Text import Text
from components.Button import Button
from components.Img import Img
from EditPeli_Admin import EditAdmin

def BusquedaDePeliculas(parent, infoUser, busqueda, tipoDeBusqueda, peliculas, ventana):
    from Salas import Salas
    def Ventana(infoPelicula, idUsuario):
        print(infoPelicula)
        # Mostrar la sala de la película seleccionada
        frame2 = Salas(ventana=ventana, infoPelicula=infoPelicula, idUsuario=idUsuario)

    def VentanaAdmin(infoPelicula, infoUser):
        # Mostrar la ventana de edición para la película seleccionada
        frame2 = EditAdmin(ventana=ventana, infoUser=infoUser, infoPelicula=infoPelicula)

    
    # Si no hay películas, no se muestra nada
    if not peliculas:
        return
    
    # Crear un marco para las películas
    frame = ctk.CTkFrame(parent, corner_radius=20)
    frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    fila = 1
    columna = 0

    # Iterar sobre las películas para crear widgets de visualización
    for pelicula in peliculas:
        # Crear un marco para la película
        marco_pelicula = ctk.CTkFrame(frame, corner_radius=10, border_width=2)
        marco_pelicula.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

        # Mostrar la imagen de la película
        Img(marco_pelicula, pelicula["img"])

        # Crear un marco para el nombre de la película
        marco_nombre = ctk.CTkFrame(marco_pelicula, fg_color="transparent") 
        marco_nombre.grid(row=1, column=0, pady=(0, 10))

        # Mostrar el nombre y duración de la película
        Text(marco_nombre, texto=pelicula["nombre"], tamanio=16).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        Text(marco_nombre, texto=f"Duración: {pelicula['dura']}H", tamanio=16).grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Botón para ver más detalles o editar la película
        if infoUser["admin"]:
            # Crear un botón para editar la película (solo para administradores)
            Button(marco_pelicula, texto="Editar", tamanio=16, eventoClick=lambda infoPelicula=pelicula, infoUser=infoUser: VentanaAdmin(infoPelicula, infoUser)).grid(row=4, column=0, padx=10, pady=5)
        else:
            # Crear un botón para ver la sala de la película
            Button(marco_pelicula, texto="Ver", tamanio=16, eventoClick=lambda infoPelicula=pelicula, idUsuario=infoUser["id"]: Ventana(infoPelicula, idUsuario)).grid(row=4, column=0, padx=10, pady=5)
       
        # Actualizar las posiciones de fila y columna
        columna += 1
        if columna >= 4:
            columna = 0
            fila += 1