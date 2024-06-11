import requests
from io import BytesIO
from PIL import Image, ImageTk
import customtkinter as ctk

def Img(f, url):
    # Realizar la solicitud GET para obtener la imagen
    res = requests.get(url)
    
    # Abrir la imagen desde el contenido de la respuesta
    img = Image.open(BytesIO(res.content))
    
    # Redimensionar la imagen a un tamaño específico
    img = img.resize((200, 200))
    
    # Convertir la imagen PIL a un objeto Image de customtkinter
    ctk_img = ImageTk.PhotoImage(img)
    
    # Crear un CTkLabel con la imagen y el texto vacío
    label = ctk.CTkLabel(f, image=ctk_img, text="", compound=ctk.TOP)
    
    # Asegurarse de mantener una referencia a la imagen para evitar que sea eliminada por el recolector de basura
    label.image = ctk_img
    
    # Colocar el CTkLabel en el marco
    label.grid(padx=10, pady=10, row=0, column=0)
    
    return label
