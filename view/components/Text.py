# components/Text.py
import customtkinter as ctk

def Text(parent, texto, tamanio, row=0, column=0, pady=10, padx=20): 
    # Creación de un CTkLabel con estilo moderno
    label = ctk.CTkLabel(parent, 
                         text=texto, 
                         font=("Arial", tamanio), 
                         pady=pady, 
                         padx=padx,
                         bg_color="transparent")

    # Configuración de la posición del label en la cuadrícula
    label.grid(row=row, column=column, sticky="w", padx=padx, pady=pady)

    return label
