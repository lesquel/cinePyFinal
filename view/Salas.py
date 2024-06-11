from layout import Layout
import customtkinter as ctk

def Salas(ventana, infoPelicula, idUsuario):
    from Sillas import Sillas
    from hooks.Peticiones.Get import GetData
    
    # Mis componentes
    from components.Text import Text
    from components.Button import Button
    from components.Regresar import Regresar
    from components.Img import Img
    
    # Información de la película
    info = [ventana, infoPelicula["id"], infoPelicula["img"], infoPelicula["nombre"]]
    
    # Obtener funciones de la película
    # funciones = GetData(f"getFunciones?idPelicula={infoPelicula['id']}")
    from datos.funciones import funciones as  funaa
    def buscarPorIdPelicula(idPelicula):
        return [funcion for funcion in funaa if funcion["idPeliculas"] == idPelicula]
    funciones = buscarPorIdPelicula(idPelicula=infoPelicula["id"])

    print(funciones)
    # Crear el marco principal utilizando la plantilla de Layout
    frame = Layout(ventana=ventana)
    
    # Configurar el grid para el marco principal
    frame.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")
    frame.grid_columnconfigure(1, weight=1)  # Aseguramos que la columna 1 se expanda
    
    # Crear frame1 y frame2 como hijos de frame
    frame1 = ctk.CTkFrame(frame, width=600, height=600)
    frame1.grid(row=0, column=0,padx=40, pady=40, sticky="nsew")
    frame1.grid_columnconfigure(0, weight=0)
    frame1.grid_columnconfigure(1, weight=1) 
    
    frame2 = ctk.CTkFrame(frame)
    frame2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    # Agregar componentes al frame principal (frame1)
    Text(parent=frame1, texto=f"Pelicula: {infoPelicula["nombre"]}", tamanio=20, row=0, column=1, padx=10, pady=20)
    Text(parent=frame1, texto=f"Descripcion: {infoPelicula["descri"]}", tamanio=16, row=1, column=1, padx=10, pady=20).configure(wraplength=400)
    Text(parent=frame1, texto=f"Duracion: {infoPelicula["dura"]}H", tamanio=16, row=2, column=1, padx=10, pady=20)
    Img(frame1, infoPelicula["img"])  # Asegurar que Img use grid
    
    # Manejar el caso donde no hay funciones
    if not funciones:
        Text(parent=frame2, texto="No hay funciones", tamanio=20, row=2, column=1, padx=10, pady=10)
        return frame

    # Función para cambiar a la ventana de selección de sillas
    def Ventana(fun, info):
        frame2 = Sillas(ventana, fun, info, idUsuario)
        frame.grid_forget()
        frame2.grid(row=0, column=0, sticky="nsew")
        Regresar(frame, frame2)

    # Posicionamiento inicial
    fila = 2
    columna = 0

    # Iterar sobre las funciones para crear los marcos
    from datos.salas import salsas
    for i, v in enumerate(funciones):
        if i % 2 == 0:
            fila += 1
            columna = 0
        
        # Crear el marco para cada función
        f = ctk.CTkFrame(frame2, border_width=2, corner_radius=10)
        f.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")
        columna += 1

        # Obtener información de la sala
        # sala = GetData(f"getSalas?idSalas={v['idSala']}")
        buscarIdSala = lambda idSala: next((s for s in salsas if s["id"] == idSala), None)
        sala = buscarIdSala(idSala=v["idSala"])
        print(sala)
        
        # Añadir texto de fecha y nombre de sala
        Text(parent=f, texto=f"Fecha: {v['fecha']}", tamanio=16, row=0, column=0, padx=5, pady=5)
        Text(parent=f, texto=sala['nombre'], tamanio=16, row=1, column=0, padx=5, pady=5)
        
        # Añadir botón de "Ver"
        Button(parent=f, texto="Ver", tamanio=16, row=2, column=0, eventoClick=lambda fun=v, info=info: Ventana(fun, info))
    
    return frame
