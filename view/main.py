import customtkinter as ctk
from login import login

# Configuración global para customtkinter
ctk.set_appearance_mode("dark")  # Tema oscuro
ctk.set_default_color_theme("dark-blue")

# Crear la ventana principal
ventana = ctk.CTk()
ventana.title("Cine")
# Obtener la resolución de la pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Configurar la ventana para que ocupe el 100% de la pantalla
ventana.geometry(f"{screen_width}x{screen_height-25}+0+0")
# Hacer que la ventana ocupe el 100% de la pantalla y deshabilitar el cambio de tamaño
ventana.resizable(False, False)  # Deshabilitar el cambio de tamaño de la ventana
# Iniciar la pantalla de login
login(ventana)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
