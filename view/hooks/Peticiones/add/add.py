def agregar_datos(entries, campos, refrescar_tabla, datos, table_frame):
    import customtkinter as ctk
    nuevo_dato = {campo: entries[campo].get() for campo in campos}
    datos.append(nuevo_dato)
    print(f"Nuevo dato agregado: {nuevo_dato}")
    for campo in campos:
        entries[campo].delete(0, ctk.END)
    refrescar_tabla(table_frame, datos, campos, entries)  # Refresca la tabla para mostrar el nuevo dato