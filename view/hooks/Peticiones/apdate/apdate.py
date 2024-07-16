def editar_dato(indice, datos, campos, entries):
    import customtkinter as ctk
    dato = datos[indice]
    print(f"Editar dato en índice {indice}: {dato}")
    for campo in campos:
        entries[campo].delete(0, ctk.END)
        entries[campo].insert(0, dato[campo])