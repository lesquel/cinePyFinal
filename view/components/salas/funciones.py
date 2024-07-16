def Funciones(parent, idUsuario, frame, ventana, funciones, info):
    import customtkinter as ctk
    from Sillas import Sillas
    from components.Text import Text
    from components.Button import Button
    # Función para cambiar a la ventana de selección de sillas
    def Ventana(fun, info):
        frame2 = Sillas(ventana, fun, info, idUsuario)
    # Posicionamiento inicial
    fila = 2
    columna = 0

    # Iterar sobre las funciones para crear los marcos
    from datos.salas import salsas
    for i, v in enumerate(funciones):
        if i % 2 == 0:
            fila += 1
            columna = 0
        
        # Crear el marco para cada función
        f = ctk.CTkFrame(parent, border_width=2, corner_radius=10)
        f.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")
        columna += 1

        # Obtener información de la sala
        # sala = GetData(f"getSalas?idSalas={v['idSala']}")
        buscarIdSala = lambda idSala: next((s for s in salsas if s["id"] == idSala), None)
        sala = buscarIdSala(idSala=v["idSala"])
        
        # Añadir texto de fecha y nombre de sala
        Text(parent=f, texto=f"Fecha: {v['fecha']}", tamanio=16, row=0, column=0, padx=5, pady=5)
        Text(parent=f, texto=sala['nombre'], tamanio=16, row=1, column=0, padx=5, pady=5)
        
        # Añadir botón de "Ver"
        Button(parent=f, texto="Ver", tamanio=16, row=2, column=0, eventoClick=lambda fun=v, info=info: Ventana(fun, info))
