import requests
from tkinter import messagebox
from components.tablaCrud.tablaStreno import TablaEstreno
from components.tablaCrud.tablaSlide import TablaSlide
def insertSlider(idPelicula, ventana, infoUser, main_frame):
    # Realizar la solicitud GET para obtener la imagen
    response = requests.get(f"http://localhost:8080/introSlider?idPelicula={idPelicula}")
    messagebox.showinfo("Insertar Slider", "El slider se ha insertado correctamente")
    TablaSlide(infoUser=infoUser, ventana=ventana, main_frame=main_frame)
    return response.json()
def insertEstreno(idPelicula, ventana, infoUser, main_frame):
    # Realizar la solicitud GET para obtener la imagen
    response = requests.get(f"http://localhost:8080/introEstrenos?idPelicula={idPelicula}")
    messagebox.showinfo("Insertar Estreno", "El estreno se ha insertado correctamente")
    TablaEstreno(infoUser=infoUser, ventana=ventana, main_frame=main_frame)
    return response.json()