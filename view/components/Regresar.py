#from .Button import Button
import customtkinter as ctk
def RegresarFunc(frame1, funFramereegre):
    def regresar_func():
        frame1.destroy()
        funFramereegre()
    boton = ctk.CTkButton(frame1, text="Regresar", command=regresar_func)
    boton.place(relx=0, rely=0, anchor='nw')