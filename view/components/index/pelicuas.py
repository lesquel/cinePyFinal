import customtkinter as ctk
from components.Text import Text
from components.Button import Button
from components.Img import Img
from hooks.Peticiones.GetPeli import GetAllPeli
from EditPeli_Admin import EditAdmin
from Salas import Salas

def Pelicuas(parent, infoUser, ventana, page=1):
    from hooks.destuirTodo import destuirTodo
    destuirTodo(ventana=parent)
    def Ventana(infoPelicula, idUsuario):
        # Mostrar la sala de la película seleccionada
        frame2 = Salas(ventana=ventana, infoPelicula=infoPelicula, idUsuario=idUsuario)

    def VentanaAdmin(infoPelicula, infoUser):
        # Mostrar la ventana de edición para la película seleccionada
        frame2 = EditAdmin(ventana=ventana, infoUser=infoUser, infoPelicula=infoPelicula)

    # Obtener películas de la página actual
    peliculas = GetAllPeli(page=page, limit=4)
    
    # Si no hay películas, no se muestra nada
    if not peliculas:
        ctk.CTkLabel(parent, text="No hay películas", font=("Arial", 24), corner_radius=20).grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        return
    
    # Añadir título al framePeliculas
    ctk.CTkLabel(parent, text="Todas las películas", font=("Arial", 24), corner_radius=20).grid(row=0, column=0, columnspan=3, padx=10, pady=10)

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

    # Crear botones de paginación si hay más páginas disponibles
    paginacion_frame = ctk.CTkFrame(parent)
    paginacion_frame.grid(row=fila+1, column=0, pady=10, sticky="nsew")

    # Botón Anterior
    if page > 1:
        btn_anterior = Button(paginacion_frame, texto="Anterior", tamanio=16, eventoClick=lambda: Pelicuas(parent, infoUser, ventana, page=page-1))
        btn_anterior.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Botón Siguiente
    btn_siguiente = Button(paginacion_frame, texto="Siguiente", tamanio=16, eventoClick=lambda: Pelicuas(parent, infoUser, ventana, page=page+1))
    btn_siguiente.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
