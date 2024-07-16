import customtkinter as ctk
from components.Button import Button
from components.GeneroEntry import obtener_id_genero

def TablaFunciones(main_frame, infoUser, ventana):
    from hooks.destuirTodo import destuirTodo
    destuirTodo(ventana=main_frame)
    # Crear marco para las columnas fijas (id, fecha, idSala, idPeliculas, sillas)
    fixed_columns_frame = ctk.CTkFrame(main_frame)
    fixed_columns_frame.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")

    # Crear encabezados fijos para id, fecha, idSala, idPeliculas, sillas
    fixed_headers = ["id", "fecha", "idSala", "idPeliculas", "sillas", "Editar", "Eliminar"]
    for col, header in enumerate(fixed_headers):
        label = ctk.CTkLabel(fixed_columns_frame, text=header.capitalize(), font=('Arial', 12, 'bold'))
        label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")
    
    # Información de las funciones para la tabla (esta será reemplazada por la función que obtenga las funciones)
    from hooks.Peticiones.GetFunciones import getAllFunciones
    funciones = getAllFunciones()
    
    if not funciones:
        print("No hay más datos para mostrar")
        return
    
    from hooks.Peticiones.apdate.apdateFuncion import apdateFuncion
    from hooks.Peticiones.delete.deleteFuncion import deleteFuncion

    def actualizar_Ventana(funcion):
        from components.VentaDeHelp import VentaDeHelp
        ventanaActualizar = VentaDeHelp(ventana, infoUser)
        
        # Datos para los selectores
        from hooks.Peticiones.GetSalas import GetAllSalas
        from hooks.Peticiones.GetPeli import GetPeliTodasAll
        salas = GetAllSalas()
        peliculas = GetPeliTodasAll()
        sala_nombres = [sala["nombre"] + f" ({sala['id']})" for sala in salas]
        pelicula_nombres = [pelicula["nombre"] + f" ({pelicula['id']})" for pelicula in peliculas]

        label_fecha_actualizar = ctk.CTkLabel(ventanaActualizar, text="Fecha")
        label_fecha_actualizar.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_fecha_actualizar = ctk.CTkEntry(ventanaActualizar, width=150)
        entry_fecha_actualizar.insert(0, funcion["fecha"])
        entry_fecha_actualizar.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        label_idSala_actualizar = ctk.CTkLabel(ventanaActualizar, text="idSala")
        label_idSala_actualizar.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_idSala_actualizar = ctk.CTkComboBox(ventanaActualizar, values=sala_nombres, width=150)
        entry_idSala_actualizar.set(f"{funcion['idSala']} ({funcion['idSala']})")  # Set initial value
        entry_idSala_actualizar.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        label_idPeliculas_actualizar = ctk.CTkLabel(ventanaActualizar, text="idPeliculas")
        label_idPeliculas_actualizar.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        entry_idPeliculas_actualizar = ctk.CTkComboBox(ventanaActualizar, values=pelicula_nombres, width=150)
        entry_idPeliculas_actualizar.set(f"{funcion['idPeliculas']} ({funcion['idPeliculas']})")  # Set initial value
        entry_idPeliculas_actualizar.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        actualizar_funcion_botones = ctk.CTkButton(ventanaActualizar, text="Actualizar", command=lambda funcion=funcion: apdateFuncion(
            id=funcion["id"], 
            fecha=entry_fecha_actualizar.get(), 
            idSala= obtener_id_genero(entry_idSala_actualizar.get()),  # Extrae solo el ID
            idPeliculas=obtener_id_genero(entry_idPeliculas_actualizar.get()),  # Extrae solo el ID
            ventana=ventana, 
            infoUser=infoUser, 
            ventanaHelp=ventanaActualizar, 
            main_frame=main_frame))
        actualizar_funcion_botones.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    
    def ver_sillas(funcion):
        from Sillas import Sillas
        from hooks.Peticiones.GetSalas import GetSalas
        sala = GetSalas(idSala=funcion["idSala"])
        from hooks.Peticiones.GetPeli import GetPeliId
        info = GetPeliId(idPelicula=funcion["idPeliculas"])
        Sillas(ventana=ventana, fun=funcion, info=info, idUsuario=infoUser["id"], funcion=funcion, sala=sala)
    
    # Insertar datos en la tabla fija (id, fecha, idSala, idPeliculas, sillas y botones de acción)
    for row, funcion in enumerate(funciones, start=1):
        fixed_data = [funcion["id"], funcion["fecha"], funcion["idSala"], funcion["idPeliculas"]]
        for col, dato in enumerate(fixed_data):
            cell = ctk.CTkLabel(fixed_columns_frame, text=str(dato), font=('Arial', 12))
            cell.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")
        
        # Botón para ver sillas
        ver_sillas_button = ctk.CTkButton(fixed_columns_frame, text="Ver", command=lambda funcion=funcion: ver_sillas(funcion))
        ver_sillas_button.grid(row=row, column=len(fixed_data), padx=10, pady=5)
        
        # Botón Editar
        edit_button = ctk.CTkButton(fixed_columns_frame, text="Editar", command=lambda funcion=funcion: actualizar_Ventana(funcion))
        edit_button.grid(row=row, column=len(fixed_data) + 1, padx=10, pady=5)
        
        # Botón Eliminar
        delete_button = ctk.CTkButton(fixed_columns_frame, text="Eliminar", command=lambda funcion=funcion: deleteFuncion(id=funcion["id"], main_frame=main_frame, infoUser=infoUser, ventana=ventana))
        delete_button.grid(row=row, column=len(fixed_data) + 2, padx=10, pady=5)
    
    # Crear marco para el formulario a la derecha
    form_frame = ctk.CTkFrame(main_frame)
    form_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
    form_frame.grid_rowconfigure(0, weight=1)
    form_frame.grid_columnconfigure(0, weight=0)  # Columna de la etiqueta
    form_frame.grid_columnconfigure(1, weight=0)  # Columna del entry

    # Datos para los selectores
    from hooks.Peticiones.GetSalas import GetAllSalas
    from hooks.Peticiones.GetPeli import GetPeliTodasAll
    salas = GetAllSalas()
    peliculas = GetPeliTodasAll()
    # Listas de nombres para los selectores
    sala_nombres = [sala["nombre"] + f" ({sala['id']})" for sala in salas]
    pelicula_nombres = [pelicula["nombre"] + f" ({pelicula['id']})" for pelicula in peliculas]

    # Etiquetas y campos de entrada en el formulario para agregar una nueva función
    ctk.CTkLabel(form_frame, text="Fecha:").grid(row=0, column=0, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    entry_fecha = ctk.CTkEntry(form_frame, width=150)  # Ancho fijo de 150
    entry_fecha.grid(row=0, column=1, padx=10, pady=5, sticky="w")  # Alineado a la izquierda

    ctk.CTkLabel(form_frame, text="idSala:").grid(row=1, column=0, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    entry_idSala = ctk.CTkComboBox(form_frame, values=sala_nombres, width=150)  # Ancho fijo de 150
    entry_idSala.grid(row=1, column=1, padx=10, pady=5, sticky="w")  # Alineado a la izquierda

    ctk.CTkLabel(form_frame, text="idPeliculas:").grid(row=2, column=0, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    entry_idPeliculas = ctk.CTkComboBox(form_frame, values=pelicula_nombres, width=150)  # Ancho fijo de 150
    entry_idPeliculas.grid(row=2, column=1, padx=10, pady=5, sticky="w")  # Alineado a la izquierda

    from hooks.Peticiones.insert.insertFuncion import insertFuncion
    agregar_button = Button(form_frame, texto="Agregar", tamanio=20, eventoClick=lambda: insertFuncion(
        fecha=entry_fecha.get(),
        idSala=obtener_id_genero(entry_idSala.get()),  # Extrae solo el ID
        idPeliculas=obtener_id_genero(entry_idPeliculas.get()),  # Extrae solo el ID
        ventana=ventana,
        infoUser=infoUser,
        main_frame=main_frame
    ))
    agregar_button.grid(row=4, columnspan=2, pady=10, padx=10)
