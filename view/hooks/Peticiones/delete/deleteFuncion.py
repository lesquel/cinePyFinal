import requests
from tkinter import messagebox
def deleteFuncion(id, main_frame, infoUser, ventana):
    respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar esta función?")
    if not respuesta:
        return None
    url = f"http://localhost:8080/deleteFunciones?id={id}"
    response = requests.get(url)
    from components.tablaCrud.tablaFunciones import TablaFunciones
    TablaFunciones(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    return response.json()