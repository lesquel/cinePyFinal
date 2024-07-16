def Comentarios(parent, idPelicula, idUsuario):
    from hooks.destuirTodo import destuirTodo
    destuirTodo(parent)
    from components.Text import Text
    import customtkinter as ctk
    from components.Button import Button

    from hooks.Peticiones.GetComentarios import GetComentarios
    comentarios = GetComentarios(idPelicula)
    
    # Crear el marco principal utilizando la plantilla de Layout
    frame = ctk.CTkFrame(parent, corner_radius=10, border_width=2)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Configurar las filas y columnas del grid principal
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    frameForm = ctk.CTkFrame(frame, corner_radius=10, border_width=2)
    frameForm.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    from hooks.Peticiones.insert.insertComentario import insertComentario
    entry_comentario = ctk.CTkEntry(frameForm, placeholder_text="Escribe un comentario...", width=750, height=40)
    entry_comentario.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    Button(parent=frameForm, texto="Enviar", tamanio=16, row=1, column=0, eventoClick=lambda: insertComentario(idPelicula=idPelicula, comentario=entry_comentario.get(), parent=parent, idUsuario=idUsuario))

    frameTodosLosComentarios = ctk.CTkFrame(parent, corner_radius=10, border_width=2)
    frameTodosLosComentarios.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Configurar el grid para que los frames hijos se expandan
    frameTodosLosComentarios.grid_rowconfigure(0, weight=1)
    frameTodosLosComentarios.grid_columnconfigure(0, weight=1)
    frameTodosLosComentarios.grid_columnconfigure(1, weight=1)  # Añadir más columnas según sea necesario

    Text(parent=frameTodosLosComentarios, texto="Comentarios", tamanio=20, row=0, column=0, padx=10, pady=10)

    from hooks.Peticiones.GetUser import GetUserId

    fila = 0
    columna = 0
    if comentarios == None:
        return
    for i, v in enumerate(comentarios):
        # Crear el marco para cada comentario
        f = ctk.CTkFrame(frameTodosLosComentarios, border_width=2, corner_radius=10)
        f.grid(row=fila + 1, column=columna, padx=10, pady=10, sticky="nsew")

        # Configurar el frame para que se expanda dentro de su celda
        f.grid_rowconfigure(0, weight=1)
        f.grid_columnconfigure(0, weight=1)

        # Mostrar el comentario
        Text(parent=f, texto=v["comentario"], tamanio=18, row=0, column=0, padx=10, pady=10)

        user = GetUserId(v["id_usuario"])
        # Mostrar el nombre del usuario que escribió el comentario
        Text(parent=f, texto=f"Escrito por: {user['name']}", tamanio=16, row=1, column=0, padx=10, pady=10)

        if columna == 1:
            fila += 1
            columna = 0
        else:
            columna += 1
