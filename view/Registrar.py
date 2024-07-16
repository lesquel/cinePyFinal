import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk

def Registrar():
    # Crear nueva ventana para el registro
    registro_ventana = ctk.CTk()
    registro_ventana.title("Registro")
    registro_ventana.geometry("900x700")

    # Crear el marco principal en la ventana de registro
    main_frame = ctk.CTkScrollableFrame(registro_ventana, width=900)
    main_frame.pack(pady=20, padx=20, fill="both", expand=True)

    def seleccionar_imagen():
        ruta_imagen = filedialog.askopenfilename(filetypes=[("Imagenes", "*.jpg;*.jpeg;*.png")])
        if ruta_imagen:
            cargar_imagen(ruta_imagen)

    def cargar_imagen(ruta):
        img_entry.delete(0, ctk.END)  # Limpiar la entrada de texto
        img_entry.insert(0, ruta)
        imagen = Image.open(ruta)
        imagen = imagen.resize((300, 300))
        global foto  # Mantener una referencia global a la imagen para evitar errores de recolección de basura
        foto = ImageTk.PhotoImage(imagen)
        label_imagen.configure(image=foto)
        label_imagen.image = foto

    label_imagen = ctk.CTkLabel(main_frame, image=None, text="")
    label_imagen.grid(row=0, column=0, columnspan=2, pady=10)

    # Título del formulario de registro
    ctk.CTkLabel(main_frame, text="Formulario de Registro", font=("Arial", 24, "bold")).grid(row=1, column=0, columnspan=2, pady=10)

    # Campos del formulario
    ctk.CTkLabel(main_frame, text="Nombre:", font=("Arial", 16)).grid(row=2, column=0, pady=5, padx=10, sticky="e")
    nombre_entry = ctk.CTkEntry(main_frame, font=("Arial", 16), width=40)
    nombre_entry.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    ctk.CTkLabel(main_frame, text="Imagen (Ruta):", font=("Arial", 16)).grid(row=3, column=0, pady=5, padx=10, sticky="e")
    img_entry = ctk.CTkEntry(main_frame, font=("Arial", 16), width=40)
    img_entry.grid(row=3, column=1, pady=5, padx=10, sticky="w")
    img_button = ctk.CTkButton(main_frame, text="Seleccionar", font=("Arial", 16), command=seleccionar_imagen)
    img_button.grid(row=3, column=2, pady=5, padx=10)

    ctk.CTkLabel(main_frame, text="Edad:", font=("Arial", 16)).grid(row=4, column=0, pady=5, padx=10, sticky="e")
    edad_entry = ctk.CTkEntry(main_frame, font=("Arial", 16), width=40)
    edad_entry.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    ctk.CTkLabel(main_frame, text="Nombre de Usuario:", font=("Arial", 16)).grid(row=5, column=0, pady=5, padx=10, sticky="e")
    usuario_entry = ctk.CTkEntry(main_frame, font=("Arial", 16), width=40)
    usuario_entry.grid(row=5, column=1, pady=5, padx=10, sticky="w")

    ctk.CTkLabel(main_frame, text="Correo:", font=("Arial", 16)).grid(row=6, column=0, pady=5, padx=10, sticky="e")
    correo_entry = ctk.CTkEntry(main_frame, font=("Arial", 16), width=40)
    correo_entry.grid(row=6, column=1, pady=5, padx=10, sticky="w")

    ctk.CTkLabel(main_frame, text="Contraseña:", font=("Arial", 16)).grid(row=7, column=0, pady=5, padx=10, sticky="e")
    contrasena_entry = ctk.CTkEntry(main_frame, show="*", font=("Arial", 16), width=40)
    contrasena_entry.grid(row=7, column=1, pady=5, padx=10, sticky="w")

    # Función para manejar el evento de "Registrar"
    from hooks.Peticiones.Registrar.registrar import registrar  # Asegúrate de que esta función está definida correctamente
    registrar_button = ctk.CTkButton(main_frame, text="Registrar", font=("Arial", 16), 
                                     command=lambda: registrar(registro_ventana, 
                                                               [nombre_entry, img_entry, edad_entry, 
                                                                usuario_entry, correo_entry, contrasena_entry]))
    registrar_button.grid(row=8, column=0, columnspan=2, pady=20)

    # Botón para cerrar la ventana de registro
    cerrar_button = ctk.CTkButton(main_frame, text="Cerrar", font=("Arial", 16), command=registro_ventana.destroy)
    cerrar_button.grid(row=9, column=0, columnspan=2, pady=10)

    # Mostrar la ventana de registro
    registro_ventana.mainloop()
