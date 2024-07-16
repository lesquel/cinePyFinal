def Tiket(parent, matriz, idUsuario, infoPelicula, funcion, sala):  
    sillas = matriz
    siHay = False
    for i, v in enumerate(matriz):
        for j, v2 in enumerate(v):
            if v2 == "S":
                siHay = True
                break
    if siHay == False:
       from tkinter import messagebox
       messagebox.showinfo("Error", "No tienes asiento ")
       return
    
    import customtkinter as ctk
    from components.Text import Text
    Text(parent=parent, texto="Tiket", tamanio=16, row=1, column=0, padx=10, pady=10)
    textBox = ctk.CTkTextbox(parent, height=150, width=200)
    textBox.grid(row=2, column=0, padx=40, pady=40, sticky="nsew")
    from components.Text import Text
    textBox.insert("end", f"Pelicula: {infoPelicula['nombre']}\n")
    textBox.insert("end", f"Sala: {sala['nombre']}\n")
    textBox.insert("end", f"Fecha: {funcion['fecha']}\n")
    textBox.insert("end", f"Duracion: {infoPelicula['dura']}H\n")
    textBox.insert("end", f"Sillas :\n")   
    for i, v in enumerate(matriz):
        for j, v2 in enumerate(v):
            if v2 == "S":
                textBox.insert("end", f"{i} {j}\n")
            elif v2 == idUsuario:
                textBox.insert("end", f"{i} {j}\n")
    from components.Button import Button
    from hooks.Guardar_tiket import Guardar_tiket
    Button(parent=parent, texto="Reservar y Cargar", tamanio=16, row=3, column=0, eventoClick=lambda: Guardar_tiket(matriz=matriz, idUsuario=idUsuario, infoPelicula=infoPelicula, funcion=funcion, sala=sala))
        