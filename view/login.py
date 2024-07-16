from layout import Layout
import customtkinter as ctk
from components.Text import Text 
from tkinter import messagebox
from hooks.login.autentificacion import autentificacion
from hooks.destuirTodo import destuirTodo

def login(ventana):
    # Crear y configurar el marco principal usando Layout
    main_frame = Layout(ventana=ventana)

    # Crear el marco para la imagen
    img_frame = ctk.CTkFrame(main_frame)
    img_frame.grid(row=0, column=0, padx=150, pady=150, sticky="nsew")

    from components.ImgLocal import Img
    from datos.UrlImgs import UrlImgsLogin
    img = Img(url_or_path=UrlImgsLogin["intercine"], tamanio=300)
    labelimg = ctk.CTkLabel(img_frame, image=img, text="", compound=ctk.TOP)
    labelimg.grid(row=0, column=0, padx=10, pady=10)

    Text(img_frame, texto="Intercine", row=1, column=0, tamanio=30)

    # Crear el marco para el formulario
    form_frame = ctk.CTkFrame(main_frame)
    form_frame.grid(row=0, column=1, padx=100, pady=150, sticky="nsew")

    Text(form_frame, texto="Ingresa a Intercine", row=0, column=0, tamanio=20)

    # Añadir campos de texto al formulario
    Text(form_frame, texto="Usuario", row=1, column=0, tamanio=16)
    usuario_entry = ctk.CTkEntry(form_frame, font=("Arial", 16), width=200, height=35)
    usuario_entry.grid(row=1, column=1, padx=10, pady=10)  # Añadir padding

    Text(form_frame, texto="Contraseña", row=2, column=0, tamanio=16)
    contrasena_entry = ctk.CTkEntry(form_frame, show="*", font=("Arial", 16), width=200, height=35)  # Para ocultar la contraseña
    contrasena_entry.grid(row=2, column=1, padx=10, pady=10)  # Añadir padding

    # Función para manejar el evento de "Entrar"
    def Entrar(ventana):    
        usuario = usuario_entry.get()
        contrasena = contrasena_entry.get()
        frame2 = autentificacion(ventana, usuario, contrasena)

    # Añadir botones al formulario con estilo y eventos
    entrar_btn = ctk.CTkButton(form_frame, text="Entrar", width=120, height=40, fg_color="blue", command=lambda: Entrar(ventana))
    entrar_btn.grid(row=3, column=1, padx=10, pady=20, sticky="e")

    from Registrar import Registrar
    registrar_btn = ctk.CTkButton(form_frame, text="Registrar", width=120, height=40, fg_color="blue", command=lambda: Registrar())
    registrar_btn.grid(row=3, column=0, padx=10, pady=20, sticky="e")

    cerrar_btn = ctk.CTkButton(form_frame, text="Cerrar", width=120, height=40, fg_color="red", command=lambda: ventana.destroy())
    cerrar_btn.grid(row=4, column=1, padx=10, pady=10, sticky="e")

    return main_frame
