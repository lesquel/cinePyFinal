def infoAdministrar(frame, infoFrame, VentanaAbrir):
    import customtkinter as ctk
    from components.Text import Text
    from components.ImgLocal import Img
    from components.Button import Button

    frameaction = ctk.CTkFrame(frame, border_color="grey", border_width=1, corner_radius=10)
    frameaction.grid(row=infoFrame["row"], column=infoFrame["column"], padx=20, pady=20, sticky="nsew")
    Text(parent=frameaction, texto=infoFrame["nombre"], tamanio=20, row=0, column=0, padx=10, pady=10)
    imgpelicula = ctk.CTkLabel(frameaction, image=Img(url_or_path=infoFrame["img"]), text="")
    imgpelicula.grid(row=1, column=0, padx=10, pady=10)
    Button(parent=frameaction, texto="Administrar", tamanio=16, row=2, column=0, eventoClick=lambda: VentanaAbrir())
    return frameaction