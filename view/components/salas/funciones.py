def Funciones(parent, idUsuario, frame, ventana, funciones, info):
    import customtkinter as ctk
    from Sillas import Sillas
    from components.Text import Text
    from components.Button import Button
    # Función para cambiar a la ventana de selección de sillas
    def Ventana(fun, info, funcion, sala):
        frame2 = Sillas(ventana, fun, info, idUsuario, funcion, sala)
    # Posicionamiento inicial

    frame1 = ctk.CTkFrame(parent)
    frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Iterar sobre las funciones para crear los marcos
    def EjecutarFunciones():
        fila = 2
        columna = 0
        if not funciones:
            Text(parent=frame1, texto="No hay funciones", tamanio=20, row=2, column=1, padx=10, pady=10)
            return frame
        for i, v in enumerate(funciones):
            if i % 3 == 0:
                fila += 1
                columna = 0
        
            # Crear el marco para cada función
            f = ctk.CTkFrame(frame1, border_width=2, corner_radius=10)
            f.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")
            columna += 1

            # Obtener información de la sala
            # sala = GetData(f"getSalas?idSalas={v['idSala']}")


            from hooks.Peticiones.GetSalas import GetSalas
            sala = GetSalas(idSala=v["idSala"])
            
            # Añadir texto de fecha y nombre de sala
            Text(parent=f, texto=f"Fecha: {v['fecha']}", tamanio=16, row=0, column=0, padx=5, pady=5)
            Text(parent=f, texto=sala['nombre'], tamanio=16, row=1, column=0, padx=5, pady=5)
            
            # Añadir botón de "Ver"
            Button(parent=f, texto="Ver", tamanio=16, row=2, column=0, eventoClick=lambda fun=v, info=info, funcion=v, sala=sala: Ventana(fun, info, funcion, sala))
    EjecutarFunciones()
    
    frame2 = ctk.CTkFrame(parent)
    frame2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    from components.Comentarios import Comentarios
    Comentarios(parent=frame2, idPelicula=info["id"], idUsuario=idUsuario)