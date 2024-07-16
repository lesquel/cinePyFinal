import customtkinter as ctk
import json

def TablaCrudPelicula(ventana, infoUser):
    from components.Button import Button  # Asumiendo que Button está correctamente definido en components.Button
    from layout import Layout  # Importa Layout si necesitas configurar la estructura de la ventana 

    # Crear el marco principal utilizando Layout
    main_frame = Layout(ventana)
    
    # Configuración del grid para expandir
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)
    
    # Función para regresar a la pantalla anterior
    from components.Regresar import RegresarFunc
    from Administrar import Administrar
    RegresarFunc(main_frame, lambda: Administrar(ventana=ventana, infoUser=infoUser))
    
    framePelicula = ctk.CTkFrame(main_frame)
    framePelicula.grid(row=0, column=0, columnspan=2, padx=20, pady=40, sticky="nsew")
    framePelicula.grid_columnconfigure(0, weight=1)
    framePelicula.grid_columnconfigure(1, weight=1)
    from components.tablaCrud.tablaPelicula import TablaPelicula
    TablaPelicula(main_frame=framePelicula, infoUser=infoUser, ventana=ventana)

    frameGenero = ctk.CTkFrame(main_frame)
    frameGenero.grid(row=1, column=0, padx=20, pady=40, sticky="nsew")
    from components.tablaCrud.tablaGenero import TablaGenero
    TablaGenero(main_frame=frameGenero, infoUser=infoUser, ventana=ventana)

    frameStreno = ctk.CTkFrame(main_frame)
    frameStreno.grid(row=2, column=0, padx=20, pady=40, sticky="nsew")
    from components.tablaCrud.tablaStreno import TablaEstreno
    TablaEstreno(main_frame=frameStreno, infoUser=infoUser, ventana=ventana)

    return main_frame
