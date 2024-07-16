import requests
from customtkinter import CTkImage
from PIL import Image

def Img(url_or_path, tamanio=75):

    try:
        # Attempt to open the image from a URL
        img = Image.open(requests.get(url_or_path, stream=True).raw)
    except (requests.exceptions.MissingSchema, OSError):
        # If fails, try to open it as a local file
        img = Image.open(url_or_path)
    
    # Resize the image as needed
    img = img.resize((tamanio, tamanio))  # Adjust the size if necessary
    
    # Convert the PIL image to a CTkImage
    ctk_img = CTkImage(light_image=img, dark_image=img, size=(tamanio, tamanio))
    
    return ctk_img
