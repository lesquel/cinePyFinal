def TablaCurdSalas(ventana, infoUser):
    import customtkinter as ctk
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
    
    frameSalas = ctk.CTkFrame(main_frame)
    frameSalas.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")
    frameSalas.grid_columnconfigure(0, weight=1)
    frameSalas.grid_columnconfigure(1, weight=1)
    from components.tablaCrud.tablaSalas import TablaSala
    TablaSala(main_frame=frameSalas, infoUser=infoUser, ventana=ventana)
    return main_frame