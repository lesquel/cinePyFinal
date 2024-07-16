import customtkinter as ctk
from tkinter import StringVar  # Importamos StringVar
from hooks.destuirTodo import destuirTodo

def EditAdmin(ventana, infoUser, infoPelicula):
    from components.Text import Text
    from components.Button import Button
    from components.Img import Img
    from components.Regresar import RegresarFunc
    from layout import Layout
    
    # Crear el marco principal
    frame = Layout(ventana)

    # Envolver los valores de las películas en StringVar para permitir la edición en los Entry
    nombre_var = StringVar(value=infoPelicula["nombre"])
    duracion_var = StringVar(value=infoPelicula["dura"])
    
    # Como CTkTextbox no utiliza textvariable, lo configuramos más adelante con el texto actual
    descripcion_text = infoPelicula["descri"]

    # Mostrar la imagen de la película
    Img(frame, infoPelicula["img"])
    
    # Crear entradas para editar la información de la película
    nombre_label = ctk.CTkLabel(frame, text="Nombre:", font=("Arial", 16), width=200, height=35)
    nombre_label.grid(row=1, column=0, padx=10, pady=10)
    nombre_entry = ctk.CTkEntry(frame, textvariable=nombre_var, width=200, height=35)
    nombre_entry.grid(row=1, column=1, padx=10, pady=10)

    duracion_label = ctk.CTkLabel(frame, text="Duración: (en horas)", font=("Arial", 16), width=200, height=35)
    duracion_label.grid(row=2, column=2, padx=10, pady=10)
    duracion_entry = ctk.CTkEntry(frame, textvariable=duracion_var, width=200, height=35)
    duracion_entry.grid(row=2, column=4, padx=10, pady=10)

    descripcion_label = ctk.CTkLabel(frame, text="Descripción:", font=("Arial", 16), width=200, height=35)
    descripcion_label.grid(row=3, column=0, padx=10, pady=10)
    
    descripcion_textbox = ctk.CTkTextbox(frame, width=400, height=100)  # Caja de texto multilinea para descripciones
    descripcion_textbox.grid(row=3, column=1, padx=10, pady=10)
    descripcion_textbox.insert("1.0", descripcion_text)  # Insertar el texto de la descripción actual
    descripcion_textbox.configure(wrap='word')  # Ajustar el texto a las palabras

    def guardar_cambios():
        # Obtener los valores actualizados de los StringVar
        newInfoPelicula = {
            "id": infoPelicula["id"],
            "nombre": nombre_var.get(),
            "descri": descripcion_textbox.get("1.0", "end-1c"),  # Obtener el texto de la caja de texto
            "dura": duracion_var.get(),
            "img": infoPelicula["img"]  # La imagen no se puede editar aquí
        }

        # Guardar los cambios (la función GuardarPeli debe estar definida en hooks.Peticiones.Guardar_peli)
        from hooks.Peticiones.Guardar_peli import GuardarPeli
        GuardarPeli(infoPelicula, newInfoPelicula)

    # Botón para guardar los cambios
    Button(frame, texto="Guardar", tamanio=16, row=4, column=0, eventoClick=guardar_cambios)

    # Función para regresar a la pantalla anterior
    from index import Index
    RegresarFunc(frame1=frame, funFramereegre=lambda: Index(ventana=ventana, infoUser=infoUser, ifAdmin=True))

    return frame
