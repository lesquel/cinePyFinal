import customtkinter as ctk
from components.Button import Button
from hooks.Peticiones.GetPeli import GetPeliId

def TablaSlide(main_frame, infoUser, ventana):
    from hooks.destuirTodo import destuirTodo
    destuirTodo(ventana=main_frame)
    
    # Crear marco para las columnas fijas (id, id_pelicula)
    fixed_columns_frame = ctk.CTkFrame(main_frame)
    fixed_columns_frame.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")

    # Información de los slides para la tabla
    from hooks.Peticiones.GetSliderAndEstreno import GetSliderAll

    def PrintarDatos():
        slides = GetSliderAll()
        if not slides:
            print("No hay datos de slides para mostrar")
        
        # Crear encabezados fijos para id y id_pelicula
        fixed_headers = ["id", "Pelicula", "Eliminar"]
        for col, header in enumerate(fixed_headers):
            label = ctk.CTkLabel(fixed_columns_frame, text=header.capitalize(), font=('Arial', 12, 'bold'))
            label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")
        
        for row, slide in enumerate(slides, start=1):
            pelicula = GetPeliId(slide["id_pelicula"])
            fixed_data = [slide["id"], pelicula["nombre"]]
            for col, dato in enumerate(fixed_data):
                cell = ctk.CTkLabel(fixed_columns_frame, text=str(dato), font=('Arial', 12))
                cell.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")
            
            # Botón Eliminar
            delete_button = ctk.CTkButton(fixed_columns_frame, text="Eliminar", command=lambda e=slide: eliminar_slide(e))
            delete_button.grid(row=row, column=len(fixed_data), padx=10, pady=5)
    
    def eliminar_slide(slide):
        from hooks.Peticiones.delete.deleteSliderAndEstreno import deleteSlider
        deleteSlider(id=slide["id"], main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    
    # Crear marco para el formulario a la derecha
    form_frame = ctk.CTkFrame(main_frame)
    form_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
    form_frame.grid_rowconfigure(0, weight=1)
    form_frame.grid_columnconfigure(0, weight=0)  # Columna de la etiqueta
    form_frame.grid_columnconfigure(1, weight=0)  # Columna del entry

    # Etiquetas y campos de entrada en el formulario para agregar un nuevo slide
    ctk.CTkLabel(form_frame, text="ID Película:").grid(row=0, column=0, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    from hooks.Peticiones.GetPeli import GetPeliTodasAll
    peliculas = GetPeliTodasAll()
    entry_id_pelicula = ctk.CTkComboBox(form_frame, values=[pelicula["nombre"] + f" ({pelicula['id']})" for pelicula in peliculas], width=150)  # Ancho fijo de 150
    entry_id_pelicula.grid(row=0, column=1, padx=10, pady=5, sticky="w")  # Alineado a la izquierda

    from hooks.Peticiones.insert.insertSliderAndEstreno import insertSlider
    from components.GeneroEntry import obtener_id_genero
    def agregar_slide():
        insertSlider(idPelicula=obtener_id_genero(entry_id_pelicula.get()), ventana=ventana, infoUser=infoUser, main_frame=main_frame)
    agregar_button = Button(form_frame, texto="Agregar", tamanio=20, eventoClick=lambda: agregar_slide())    
    agregar_button.grid(row=1, columnspan=2, pady=10, sticky="nsew")
    
    PrintarDatos()

