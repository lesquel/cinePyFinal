import customtkinter as ctk
def crear_boton(parent, text, command):
        boton = ctk.CTkButton(parent, text=text, fg_color="#333333", corner_radius=10,
                              font=("Arial", 20), width=220, height=40, command=command, hover_color="blue")
        boton.grid(padx=10, pady=5, sticky="ew")
        return boton

def Nav(frame, ventanas):
    from index import Index
    from Perfil import Perfil
    from login import login
    """
    Crea un menú lateral dentro del marco dado.
    
    Args:
        frame (CTkFrame): El marco principal donde se añadirá el menú lateral.
    """
    # Crear el marco para el menú lateral
    sidebar = ctk.CTkFrame(frame, width=220)
    sidebar.grid(row=0, column=0, sticky="ns", padx=10, pady=10)
    
    # Añadir botones al menú lateral utilizando la función crear_boton
    boton1 = crear_boton(sidebar, "Inicio", lambda: Index(ventana=ventanas[0]["ventana"], infoUser=ventanas[0]["infoUser"]))
    boton2 = crear_boton(sidebar, "Perfil", lambda: Perfil(ventana=ventanas[0]["ventana"], infoUser=ventanas[0]["infoUser"]))
    boton3 = crear_boton(sidebar, "Ajustes", lambda: print("Ajustes presionado"))
    boton4 = crear_boton(sidebar, "Cerrar Secion", lambda: login(ventanas[0]["ventana"]))

    return sidebar

def NavAdmid(frame, ventanas):
    from Administrar import Administrar
    """
    Crea un menú lateral dentro del marco dado.
    
    Args:
        frame (CTkFrame): El marco principal donde se añadirá el menú lateral.
    """
    # Crear el marco para el menú lateral
    sidebar = Nav(ventanas=ventanas, frame=frame)

    boton1 = crear_boton(sidebar, "Administrar", lambda: Administrar(ventana=ventanas[0]["ventana"], infoUser=ventanas[0]["infoUser"]))