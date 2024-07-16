from tkinter import messagebox
from hooks.Peticiones.Update import UpdateData
from hooks.Peticiones.Get import GetData
def Reservar(frame, info, id, sillas, idUsuario, funcion, sala):
        from components.Tiket import Tiket
        Tiket(parent=frame, matriz=sillas, idUsuario=idUsuario, infoPelicula=info, funcion=funcion, sala=sala)
