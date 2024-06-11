import customtkinter as ctk
def Index(ventana, infoUser):
    from components.Text import Text
    from components.Button import Button
    from hooks.Peticiones.Get import GetData
    from Salas import Salas
    from components.Regresar import Regresar
    from components.Img import Img
    from components.Nav import Nav

    # Crear el marco principal
    frame = ctk.CTkFrame(ventana, corner_radius=20)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Configurar grid para el marco principal
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    # Crear el menú lateral
    Nav(frame, [
        {"ventana": ventana, "infoUser": infoUser},
    ])

    # Crear el contenido principal en la columna adyacente
    canvas = ctk.CTkCanvas(frame, highlightthickness=0)
    canvas.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # Agregar una barra de desplazamiento vertical
    scrollbar_vertical = ctk.CTkScrollbar(frame, command=canvas.yview)
    scrollbar_vertical.grid(row=0, column=2, sticky="ns")

    # Configurar el lienzo para que funcione con la barra de desplazamiento vertical
    canvas.configure(yscrollcommand=scrollbar_vertical.set, width=790, height=600)

    # Crear un marco interior para los widgets
    frame_interior = ctk.CTkFrame(canvas)
    frame_interior.configure(width=1000, height=600)
    canvas.create_window((0, 0), window=frame_interior, anchor="nw")

    # Añadir título
    ctk.CTkLabel(frame_interior, text="Películas", font=("Arial", 24), corner_radius=20).grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # Obtener la lista de películas
    from datos.peliculas import peliculas

    def Ventana(infoPelicula, idUsuario):
        # Mostrar la sala de la película seleccionada
        frame2 = Salas(ventana=ventana, infoPelicula=infoPelicula, idUsuario=idUsuario)
        frame.grid_forget()
        frame2.grid(row=0, column=0, sticky="nsew")
        Regresar(frame, frame2)

    fila = 1
    columna = 0

    # Iterar sobre las películas para crear widgets de visualización
    for pelicula in peliculas:
        # Crear un marco para la película
        marco_pelicula = ctk.CTkFrame(frame_interior, corner_radius=10, border_width=2)
        marco_pelicula.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

        # Mostrar la imagen de la película
        Img(marco_pelicula, pelicula["img"])

        # Crear un marco para el nombre de la película
        marco_nombre = ctk.CTkFrame(marco_pelicula)
        marco_nombre.grid(pady=(0, 10))

        # Mostrar el nombre de la película
        Text(marco_nombre, texto=pelicula["nombre"], tamanio=16, row=0, column=0, padx=10, pady=10).grid(sticky="w")
        Text(marco_nombre, texto=f"Duracion: {pelicula["dura"]}H", tamanio=16, row=1, column=0, padx=10, pady=10).grid(sticky="w")

        # Crear un botón para ver más detalles de la película
        Button(marco_pelicula, texto="Ver", tamanio=16, row=2, column=0, eventoClick=lambda infoPelicula=pelicula, idUsuario=infoUser["id"]: Ventana(infoPelicula, idUsuario))

        # Actualizar las posiciones de fila y columna
        columna += 1
        if columna >= 3:
            columna = 0
            fila += 1

    # Actualizar la geometría del lienzo
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    return frame
