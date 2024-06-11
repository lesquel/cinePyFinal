import customtkinter as ctk
from layout import Layout
from index import Index
from components.Text import Text 
from hooks.Peticiones.Get import GetData
from tkinter import messagebox

# Configuración global para customtkinter
ctk.set_appearance_mode("dark")  # Tema oscuro
ctk.set_default_color_theme("dark-blue")

def Cerrar(ventana):
    ventana.destroy()  # Cierra la ventana

# Crear ventana principal
ventana = ctk.CTk()
ventana.title("Cine")
ventana.config(bg="#000000")  # Configurar el color de fondo de la ventana

# Crear y configurar el frame
frame = Layout(ventana=ventana)
frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

Text(frame, texto="Ingresa a Cinequel", row=0, column=0, tamanio=20)

# Añadir campos de texto con estilo
Text(frame, texto="Usuario", row=1, column=0, tamanio=16)
usuario_entry = ctk.CTkEntry(frame, font=("Arial", 16), width=200, height=35)
usuario_entry.grid(row=1, column=1, padx=10, pady=10)  # Añadir padding

Text(frame, texto="Contraseña", row=2, column=0, tamanio=16)
contrasena_entry = ctk.CTkEntry(frame, show="*", font=("Arial", 16), width=200, height=35)  # Para ocultar la contraseña
contrasena_entry.grid(row=2, column=1, padx=10, pady=10)  # Añadir padding

# Función para manejar el evento de "Entrar"
def Entrar(ventana):    
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()
    if usuario == "":
        messagebox.showinfo("Error", "Introduzca el usuario")
        return
    if contrasena == "":
        messagebox.showinfo("Error", "Introduzca la contraseña")
        return
    from datos.perfil import perfil
    buscarNombreContra = lambda nombre, contra: next((perfil for perfil in perfil if perfil["nombre"] == nombre and perfil["contra"] == contra), None)
    infoUser = buscarNombreContra(nombre=usuario, contra=contrasena)
    if not infoUser:
        messagebox.showinfo("Error", "Usuario o contraseña incorrectos")
        return
    frame2 = Index(ventana, infoUser=infoUser)
    frame.grid_forget()
    frame2.grid(row=0, column=0, sticky="nsew")

# Añadir botones con estilo y eventos
entrar_btn = ctk.CTkButton(frame, text="Entrar", width=120, height=40, command=lambda: Entrar(ventana))
entrar_btn.grid(row=4, column=1, padx=10, pady=20, sticky="e")

cerrar_btn = ctk.CTkButton(frame, text="Cerrar", width=120, height=40, command=lambda: Cerrar(ventana))
cerrar_btn.grid(row=5, column=1, padx=10, pady=10, sticky="e")

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
