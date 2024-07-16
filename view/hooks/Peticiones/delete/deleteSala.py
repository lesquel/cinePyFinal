import requests
from tkinter import messagebox
def deleteSala(id, main_frame, infoUser, ventana):
    # http://localhost:8080/deleteSala?id=1
    respuest = messagebox.askyesno("Eliminar", "¿Estás seguro de eliminar esta sala?")
    if not respuest:
        return
    url = f"http://localhost:8080/deleteSala?id={id}"
    requests.get(url)
    from components.tablaCrud.tablaSalas import TablaSala
    TablaSala(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    return