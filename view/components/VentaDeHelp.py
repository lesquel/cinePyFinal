def VentaDeHelp(ventana, infoUser):
    import customtkinter as ctk
    ventanaActualizar = ctk.CTkToplevel(ventana)
    ventanaActualizar.title("Actualizar género")
    ventanaActualizar.resizable(False, False)
    ventanaActualizar.transient(ventana)
    frame = ctk.CTkFrame(ventanaActualizar)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    return frame