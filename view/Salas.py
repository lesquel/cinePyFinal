from layout import Layout
import customtkinter as ctk

def Salas(ventana, infoPelicula, idUsuario):
    # Mis componentes
    from components.Text import Text
    from components.Img import Img
    from components.salas.funciones import Funciones
    # Información de la película
    info = {"ventana": ventana, "id": infoPelicula["id"], "img": infoPelicula["img"], "nombre": infoPelicula["nombre"], "descri": infoPelicula["descri"], "dura": infoPelicula["dura"]}
    
    # Obtener funciones de la película
    # funciones = GetData(f"getFunciones?idPelicula={infoPelicula['id']}")
    from datos.funciones import funciones as  funaa
    def buscarPorIdPelicula(idPelicula):
        return [funcion for funcion in funaa if funcion["idPeliculas"] == idPelicula]
    funciones = buscarPorIdPelicula(idPelicula=infoPelicula["id"])

    # Crear el marco principal utilizando la plantilla de Layout
    frame = Layout(ventana=ventana)
    
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
    
    Funciones(parent=frame2, idUsuario=idUsuario, frame=frame, ventana=ventana, funciones=funciones, info=info)

    from components.Regresar import RegresarFunc
    from index import Index
    from hooks.Peticiones.GetUser import GetUserId
    infoUser = GetUserId(idUsuario)
    RegresarFunc(frame1=frame, funFramereegre=lambda: Index(ventana=ventana, infoUser=infoUser))

    return frame
