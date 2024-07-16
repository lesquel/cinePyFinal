import customtkinter as ctk
import json

# Variable para rastrear la página actual
current_page = 1
def TablaPelicula(main_frame, infoUser, ventana, page=1):
    from hooks.destuirTodo import destuirTodo
    destuirTodo(ventana=main_frame)
    from components.Button import Button  # Asumiendo que Button está correctamente definido en components.Button
    import customtkinter as ctk
    
    global current_page
    current_page = page

    # Configuración del grid para expandir
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=0)  # Fijo
    main_frame.grid_columnconfigure(1, weight=1)  # Expansible
    main_frame.grid_columnconfigure(2, weight=0)  # Fijo
    
    # Crear marco para las columnas fijas (id, nombre, img + botones de acción)
    fixed_columns_frame = ctk.CTkFrame(main_frame)
    fixed_columns_frame.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")

    # Crear encabezados fijos para id, nombre, img, editar y eliminar
    fixed_headers = ["id", "nombre", "Editar", "Eliminar"]
    for col, header in enumerate(fixed_headers):
        label = ctk.CTkLabel(fixed_columns_frame, text=header.capitalize(), font=('Arial', 12, 'bold'))
        label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")
    
    # Crear marco para la tabla con scroll horizontal para las demás columnas
    scrollable_frame = ctk.CTkScrollableFrame(main_frame, orientation="horizontal", width=500)
    scrollable_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    # Crear encabezados de la tabla desplazable para las columnas restantes
    scrollable_headers = ["img", "genero", "duracion", "trailer", "descripcion"]
    for col, header in enumerate(scrollable_headers):
        label = ctk.CTkLabel(scrollable_frame, text=header.capitalize(), font=('Arial', 12, 'bold'))
        label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")
    
    # Información de la película para la tabla
    from hooks.Peticiones.GetPeli import GetAllPeli
    peliculas = GetAllPeli(page=page, limit=8)
    
    if not peliculas:
        print("No hay más datos para mostrar")
        return
    
    # Funciones de acción para editar y eliminar
    def editar_pelicula(pelicula):
        from EditPeli_Admin import EditAdmin
        EditAdmin(ventana=ventana, infoUser=infoUser, infoPelicula=pelicula)
        # Aquí puedes agregar la lógica para editar la película

    from hooks.Peticiones.delete.deletePeli import eliminar_pelicula

    # Insertar datos en la tabla fija (id, nombre, img y botones de acción)
    for row, pelicula in enumerate(peliculas, start=1):
        fixed_data = [pelicula["id"], pelicula["nombre"]]
        for col, dato in enumerate(fixed_data):
            cell = ctk.CTkLabel(fixed_columns_frame, text=str(dato), font=('Arial', 12))
            cell.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")
        
        # Botón Editar
        edit_button = ctk.CTkButton(fixed_columns_frame, text="Editar", command=lambda p=pelicula: editar_pelicula(p))
        edit_button.grid(row=row, column=len(fixed_data), padx=10, pady=5)
        
        # Botón Eliminar
        delete_button = ctk.CTkButton(fixed_columns_frame, text="Eliminar", command=lambda p=pelicula: eliminar_pelicula(p, main_frame=main_frame, ventana=ventana, infoUser=infoUser))
        delete_button.grid(row=row, column=len(fixed_data) + 1, padx=10, pady=5)
    
    # Insertar datos en la tabla desplazable para las demás columnas
    for row, pelicula in enumerate(peliculas, start=1):
        scrollable_data = [pelicula["img"], pelicula["genero"], pelicula["dura"], pelicula["trailer"], pelicula["descri"]]
        for col, dato in enumerate(scrollable_data):
            cell = ctk.CTkLabel(scrollable_frame, text=str(dato), font=('Arial', 12))
            cell.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")
    
    # Crear marco para el formulario a la derecha
    form_frame = ctk.CTkFrame(main_frame)
    form_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
    form_frame.grid_rowconfigure(0, weight=1)
    form_frame.grid_columnconfigure(0, weight=1)

    # Etiquetas y campos de entrada en el formulario basados en los campos proporcionados
    campos = ["nombre", "duracion", "trailer", "descripcion", "img"]
    entries = {}  # Diccionario para almacenar las referencias de los campos de entrada
    
    for idx, campo in enumerate(campos):
        ctk.CTkLabel(form_frame, text=f"{campo.capitalize()}:").grid(row=idx, column=0, padx=10, pady=5, sticky="nsew")
        entry = ctk.CTkEntry(form_frame)
        entry.grid(row=idx, column=1, padx=10, pady=5, sticky="nsew")
        entries[campo] = entry  # Almacena la referencia del campo de entrada

    from components.GeneroEntry import GeneroEntry
    genero_var, genero_menu, entries = GeneroEntry(parent=form_frame, campos=campos, entries=entries)

    from components.AbrirImg import ImgAbrir
    label_imagen = ImgAbrir(frame=form_frame, img_entry=entries["img"], row=len(campos)+1, column=1)
    
    # Botón para agregar datos al formulario
    from hooks.Peticiones.insert.insertPelicula import insertPelicula
    agregar_button = Button(form_frame, texto="Agregar", tamanio=20, eventoClick=lambda: insertPelicula(entries=entries, label_imagen=label_imagen, main_frame=main_frame, ventana=ventana, infoUser=infoUser))
    agregar_button.grid(row=len(campos)+2, columnspan=2, pady=10, sticky="nsew")
    
    def limpiar_todo():
        TablaPelicula(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    limpiar_todo = Button(form_frame, texto="Limpiar todo", tamanio=20, eventoClick=limpiar_todo)
    limpiar_todo.grid(row=len(campos)+3, columnspan=2, pady=10, sticky="nsew")

    # Agregar botones de paginación al final
    paginacion_frame = ctk.CTkFrame(main_frame)
    paginacion_frame.grid(row=1, column=0, columnspan=3, pady=20, sticky="nsew")
    paginacion_frame.grid_columnconfigure(0, weight=1)
    paginacion_frame.grid_columnconfigure(1, weight=1)
    paginacion_frame.grid_columnconfigure(2, weight=1)
    
    def pagina_anterior():
        global current_page
        if current_page > 1:
            current_page -= 1
            TablaPelicula(main_frame, infoUser, ventana, current_page)

    def pagina_siguiente():
        global current_page
        current_page += 1
        peliculas_nuevas = GetAllPeli(page=current_page, limit=8)
        if peliculas_nuevas:
            TablaPelicula(main_frame, infoUser, ventana, current_page)
        else:
            current_page -= 1  # Si no hay más datos, no incrementamos la página
    
    anterior_button = Button(paginacion_frame, texto="Anterior", tamanio=20, eventoClick=pagina_anterior)
    anterior_button.grid(row=0, column=0, pady=10, padx=20, sticky="nsew")

    siguiente_button = Button(paginacion_frame, texto="Siguiente", tamanio=20, eventoClick=pagina_siguiente)
    siguiente_button.grid(row=0, column=2, pady=10, padx=20, sticky="nsew")

    current_page_label = ctk.CTkLabel(paginacion_frame, text=f"Página {current_page}", font=('Arial', 12, 'bold'))
    current_page_label.grid(row=0, column=1, pady=10, padx=20, sticky="nsew")