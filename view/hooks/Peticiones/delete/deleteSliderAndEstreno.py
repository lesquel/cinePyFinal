import requests
from tkinter import messagebox
from components.tablaCrud.tablaStreno import TablaEstreno
from components.tablaCrud.tablaSlide import TablaSlide
def deleteSlider(id, ventana, infoUser, main_frame):
    # Realizar la solicitud GET para obtener la imagen
    respuesta = messagebox.askyesno("Eliminar Slider", "¿Estás seguro de eliminar el slider?")
    if respuesta == False:
        return
    response = requests.get(f"http://localhost:8080/deleteSlider?id={id}")
    TablaSlide(infoUser=infoUser, ventana=ventana, main_frame=main_frame)
    return response.json()
def deleteEstreno(id, ventana, infoUser, main_frame):
    # Realizar la solicitud GET para obtener la imagen
    respuesta = messagebox.askyesno("Eliminar Estreno", "¿Estás seguro de eliminar el estreno?")
    if respuesta == False:
        return
    response = requests.get(f"http://localhost:8080/deleteEstrenos?id={id}")
    TablaEstreno(infoUser=infoUser, ventana=ventana, main_frame=main_frame)
    return response.json()