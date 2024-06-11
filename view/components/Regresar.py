#from .Button import Button
import customtkinter as ctk
def Regresar(frame1, frame2):
    boton = ctk.CTkButton(frame2, text="Regresar")
    def regresar_func():
        frame2.grid_forget()
        frame1.grid()
        boton.destroy()
    # Agregar un botón de regreso al segundo frame usando pack
    boton.configure(command=regresar_func)
    boton.place(relx=0, rely=0, anchor='nw')
    #Button(parent=frame2, texto="Regresar", tamanio=16, row=20, column=6, eventoClick=regresar_func)
