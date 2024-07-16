# Función para eliminar datos
def eliminar_dato(indice, datos, refrescar_tabla, table_frame, campos, entries):
    from tkinter import messagebox
    comfirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este registro?")
    if comfirmar: 
        dato = datos[indice]
        print(f"Eliminar dato en índice {indice}: {dato}")
        datos.pop(indice)  # Elimina el dato de la lista
        refrescar_tabla(table_frame, datos, campos, entries)  # Refresca la tabla para actualizar la visualización
        return True
    else:
        return False