# view/components/AllSIllas.py
from .Sillas import Sillas
import hooks.Cambiar_Guardar as Cambiar_Guardar
from datos.UrlImgs import UrlImgs
import customtkinter as ctk

def AllSIllas(matriz, frame, idUsuario):
    fra = ctk.CTkFrame(frame)
    fra.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")
    def ejecutar2(b, r, c):
        # Usamos `nonlocal` para indicar que `matriz` no es una variable local a `ejecutar2`
        nonlocal matriz
        matriz = Cambiar_Guardar.Cambiar_Guardar(b=b, r=r, c=c, matriz=matriz)
        fra.destroy()
        AllSIllas(matriz=matriz, frame=frame, idUsuario=idUsuario)
        # Eliminar todos los widgets hijos en el frame para poder re-renderizar

    # Crear los botones para la matriz de sillas
    for i, f in enumerate(matriz):
        for j, c in enumerate(f):
            if c == "L":
                b, r, c = Sillas(parent=fra, tamanio=16, row=i, column=j, bg_color="#8888ff", imagen_url=UrlImgs["azul"])
                b.configure(command=lambda b=b, r=i, c=j: ejecutar2(b, r, c))
            elif c == "S":
                Sillas(parent=fra, tamanio=16, row=i, column=j, bg_color="#888888", imagen_url=UrlImgs["rojo"])
            elif c == "R":
                b, r, c = Sillas(parent=fra, tamanio=16, row=i, column=j, bg_color="#88ff88", imagen_url=UrlImgs["verde"])
                b.configure(command=lambda b=b, r=i, c=j: ejecutar2(b, r, c))
            elif c == idUsuario:
                b, r, c = Sillas(parent=fra, tamanio=16, row=i, column=j, bg_color="#ffff00", imagen_url=UrlImgs["amarillo"])
                b.configure(command=lambda b=b, r=i, c=j: ejecutar2(b, r, c))
            else:  # Asientos ocupados por otros usuarios
                Sillas(parent=fra, tamanio=16, row=i, column=j, bg_color="#ff8888", imagen_url=UrlImgs["negro"])