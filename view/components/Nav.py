import customtkinter as ctk
def Nav(frame, ventanas):
    from index import Index
    from Perfil import Perfil
    """
    Crea un menú lateral dentro del marco dado.
    
    Args:
        frame (CTkFrame): El marco principal donde se añadirá el menú lateral.
    """
    # Crear el marco para el menú lateral
    sidebar = ctk.CTkFrame(frame, width=150, corner_radius=10, fg_color="#333333", bg_color="#222222")
    sidebar.grid(row=0, column=0, sticky="ns", padx=10, pady=10)
    
    # Añadir botones al menú lateral
    boton1 = ctk.CTkButton(sidebar, text="Inicio", fg_color="#444444", command=lambda: Index(ventana=ventanas[0]["ventana"], infoUser=ventanas[0]["infoUser"]))
    boton1.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    boton2 = ctk.CTkButton(sidebar, text="Perfil", fg_color="#444444", command=lambda: Perfil(ventana=ventanas[0]["ventana"], infoUser=ventanas[0]["infoUser"]))
    boton2.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    boton3 = ctk.CTkButton(sidebar, text="Ajustes", fg_color="#444444", command=lambda: print("Ajustes presionado"))
    boton3.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    return sidebar