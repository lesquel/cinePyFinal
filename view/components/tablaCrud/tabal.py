def refrescar_tabla(table_frame, datos, campos, entries):
    # Elimina todas las filas de datos, manteniendo los encabezados
    from components.Button import Button
    from hooks.Peticiones.apdate.apdate import editar_dato
    from hooks.Peticiones.delete.delete import eliminar_dato
    import customtkinter as ctk
    for widget in table_frame.grid_slaves():
        if int(widget.grid_info()["row"]) > 0:
            widget.grid_forget()
    
    # Vuelve a crear las filas de datos
    for row, item in enumerate(datos, start=1):
        for col, key in enumerate(campos):
            value = item.get(key, '')  # Obtiene el valor correspondiente o una cadena vacía si no existe la clave
            label = ctk.CTkLabel(table_frame, text=str(value))
            label.grid(row=row, column=col, padx=10, pady=5)
        
        # Botón de Editar
        editar_button = Button(table_frame, texto='Editar', tamanio=18, eventoClick=lambda r=row-1: editar_dato(r, datos, campos, entries))
        editar_button.grid(row=row, column=len(campos), padx=10, pady=5)
        
        # Botón de Eliminar
        eliminar_button = Button(table_frame, texto='Eliminar', tamanio=18, eventoClick=lambda r=row-1: eliminar_dato(r, datos, refrescar_tabla, table_frame, campos, entries))
        eliminar_button.grid(row=row, column=len(campos) + 1, padx=10, pady=5)
