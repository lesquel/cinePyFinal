def obtener_id_genero(seleccion):
    if not seleccion:
        raise ValueError("La selección está vacía.")
    
    try:
        id_str = seleccion.split("(")[-1].strip(")")
        return int(id_str)
    except (IndexError, ValueError) as e:
        raise ValueError(f"Error al obtener el ID del género de '{seleccion}': {e}")

def GeneroEntry(parent, campos, entries, valorPordefecto=None):
    # Lista de géneros para el menú desplegable
    import customtkinter as ctk
    from hooks.Peticiones.getGenero import getAllGeneros
    generos = getAllGeneros()

    # Crear el menú desplegable para el género
    genero_var = ctk.StringVar()
    ctk.CTkLabel(parent, text="Género:").grid(row=len(campos), column=0, padx=10, pady=5, sticky="nsew")
    genero_menu = ctk.CTkOptionMenu(parent, values=[g["nombre"] + " (" + str(g["id"]) + ")" for g in generos], variable=genero_var)
    genero_menu.grid(row=len(campos), column=1, padx=10, pady=5, sticky="nsew")
    if valorPordefecto:
        genero_var.set(valorPordefecto)
    entries["genero"] = genero_var  # Almacena la referencia del menú desplegable en entries
    return genero_var, genero_menu, entries