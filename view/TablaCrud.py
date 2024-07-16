import customtkinter as ctk
from components.Button import Button  # Asumiendo que Button está correctamente definido en components.Button

def TablaCrud(ventana, datos, campos, infoUser):
    from layout import Layout  # Importa Layout si necesitas configurar la estructura de la ventana
    
    # Crear el marco principal utilizando Layout
    main_frame = Layout(ventana)
    
    # Función para regresar a la pantalla anterior
    from components.Regresar import RegresarFunc
    from Administrar import Administrar
    RegresarFunc(main_frame, lambda: Administrar(ventana=ventana, infoUser=infoUser))
    
    # Crear marco para la tabla con scroll horizontal
    table_frame = ctk.CTkScrollableFrame(main_frame, orientation="horizontal")
    table_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
    
    # Crear encabezados de la tabla de forma dinámica basados en los campos proporcionados
    for col, header in enumerate(campos):
        label = ctk.CTkLabel(table_frame, text=header, font=('Arial', 12, 'bold'))
        label.grid(row=0, column=col, padx=10, pady=5)
    
    
    
    # Crear marco para el formulario a la derecha
    form_frame = ctk.CTkFrame(main_frame)
    form_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    
    # Etiquetas y campos de entrada en el formulario basados en los campos proporcionados
    entries = {}  # Diccionario para almacenar las referencias de los campos de entrada
    
    for idx, campo in enumerate(campos):
        ctk.CTkLabel(form_frame, text=f"{campo.capitalize()}:").grid(row=idx, column=0, padx=10, pady=5)
        entry = ctk.CTkEntry(form_frame)
        entry.grid(row=idx, column=1, padx=10, pady=5)
        entries[campo] = entry  # Almacena la referencia del campo de entrada
    
    # Botón para agregar datos al formulario
    agregar_button = Button(form_frame, texto="Agregar", tamanio=20, eventoClick=lambda: agregar_datos(entries, campos, refrescar_tabla, datos, table_frame))
    agregar_button.grid(row=len(campos), columnspan=2, pady=10)
    
    
    from hooks.Peticiones.add.add import agregar_datos

    from components.tablaCrud.tabal import refrescar_tabla

    refrescar_tabla(table_frame, datos, campos, entries)
    
    return main_frame
