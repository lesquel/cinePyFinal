# components/Sillas.py
import customtkinter as ctk

def Sillas(parent, texto, row, column, tamanio, bg_color="#888888"):
    """
    Crea un botón estilo silla usando customtkinter con diseño moderno.
    
    Args:
        parent (widget): El contenedor padre para el botón.
        texto (str): El texto que se mostrará en el botón.
        row (int): La fila en la cuadrícula del contenedor.
        column (int): La columna en la cuadrícula del contenedor.
        tamanio (int): El tamaño de la fuente del texto del botón.
        bg (str): El color de fondo del botón.
        fg (str): El color del texto del botón.
        hover_color (str): El color de fondo del botón cuando se pasa el ratón sobre él.

    Returns:
        btn (CTkButton): El botón creado.
    """
    # Crear un botón estilo CTkButton
    btn = ctk.CTkButton(parent, 
                        text=texto, 
                        font=("Arial", tamanio),
                        border_width=3,
                        fg_color=bg_color,
                        text_color="#000000",
                        corner_radius=10,  # Radio de las esquinas para un diseño más suave
                        width=120,  # Ancho del botón
                        height=40)  # Altura del botón

    # Posicionar el botón en la cuadrícula
    btn.grid(row=row, column=column, padx=10, pady=10)  # Añadir padding para espaciar los botones

    return [btn, row, column]
