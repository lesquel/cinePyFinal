from tkinter import filedialog
from PIL import Image, ImageTk
import customtkinter as ctk
import requests
from io import BytesIO

def ImgAbrir(frame, img_entry, row, column):
    # Crear un label inicial vacío para mostrar la imagen
    def crear_label():
        laber = ctk.CTkLabel(main_frame, image=None, text="")
        laber.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        return laber

    # Seleccionar una imagen mediante un diálogo de archivo
    def seleccionar_imagen():
        ruta_imagen = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg;*.jpeg;*.png")])
        if ruta_imagen:
            cargar_imagen(ruta_imagen)

    # Seleccionar una imagen desde la entrada de texto
    def seleccionar_imagen_por_entry(event):
        ruta_imagen = img_entry.get()
        if ruta_imagen:
            cargar_imagen(ruta_imagen)

    # Cargar la imagen desde una ruta o URL
    def cargar_imagen(ruta):
        global photo
        try:
            # Verificar si la ruta es una URL
            if ruta.startswith("http://") or ruta.startswith("https://"):
                response = requests.get(ruta)
                response.raise_for_status()  # Asegurarse de que la descarga fue exitosa
                imagen = Image.open(BytesIO(response.content))
            else:
                imagen = Image.open(ruta)  # Cargar la imagen desde una ruta local

            # Redimensionar la imagen
            imagen = imagen.resize((300, 300))

            # Convertir la imagen a un objeto `PhotoImage` compatible con Tkinter
            photo = ImageTk.PhotoImage(imagen)

            # Mostrar la imagen en el `Label`
            label_imagen.configure(image=photo)
            label_imagen.image = photo  # Guardar referencia para evitar que se elimine por el recolector de basura

            # Actualizar el `Entry` con la ruta de la imagen cargada
            img_entry.delete(0, ctk.END)
            img_entry.insert(0, ruta)

        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

    # Configuración de la interfaz gráfica
    main_frame = ctk.CTkFrame(frame, fg_color="transparent")
    main_frame.grid(row=row, column=column, sticky="nsew")

    # Botón para seleccionar imagen
    btn_seleccionar = ctk.CTkButton(main_frame, text="Seleccionar Imagen", command=seleccionar_imagen)
    btn_seleccionar.grid(row=1, column=0, pady=20, padx=10)

    # Asignar evento de teclado para cargar la imagen desde el `Entry`
    img_entry.bind("<Return>", seleccionar_imagen_por_entry)

    # Crear y retornar el label de la imagen
    label_imagen = crear_label()
    return label_imagen
