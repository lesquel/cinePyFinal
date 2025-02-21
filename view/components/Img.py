import requests
from io import BytesIO
from PIL import Image
import customtkinter as ctk
from concurrent.futures import ThreadPoolExecutor

# Función que descargará y procesará la imagen en un hilo separado
def download_and_process_image(url, tamanio):
    res = requests.get(url)
    img = Image.open(BytesIO(res.content))
    img = img.resize((tamanio, tamanio))
    return img

# Función para actualizar la imagen en el GUI
def update_image(f, img, tamanio, row, column):
    # Convertir la imagen PIL a un objeto CTkImage de customtkinter
    ctk_img = ctk.CTkImage(light_image=img, size=(tamanio, tamanio))
    
    # Crear un CTkLabel con la imagen y el texto vacío
    label = ctk.CTkLabel(f, image=ctk_img, text="", compound=ctk.TOP)
    
    # Asegurarse de mantener una referencia a la imagen para evitar que sea eliminada por el recolector de basura
    label.image = ctk_img
    
    # Colocar el CTkLabel en el marco
    label.grid(padx=10, pady=10, row=row, column=column)
    
    return label

# Función para manejar la imagen asíncronamente
def handle_image(f, future, tamanio, row, column):
    if future.done():
        # Si la tarea ha terminado, obtener el resultado y actualizar la imagen en el GUI
        img = future.result()
        update_image(f, img, tamanio, row, column)
    else:
        # Si la tarea aún no ha terminado, comprobar de nuevo después de un breve período
        f.after(100, handle_image, f, future, tamanio, row, column)

def Img(f, url, tamanio=250, row=0, column=0):
    # Usar ThreadPoolExecutor para descargar y procesar la imagen en un hilo separado
    executor = ThreadPoolExecutor()
    
    # Submit una tarea para descargar y procesar la imagen
    future = executor.submit(download_and_process_image, url, tamanio)
    
    # Llamar a la función para manejar la imagen de manera asíncrona
    f.after(100, handle_image, f, future, tamanio, row, column)
