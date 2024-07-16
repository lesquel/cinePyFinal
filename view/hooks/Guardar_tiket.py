from tkinter import filedialog, messagebox
from index import Index
from hooks.Peticiones.GetUser import GetUserId

def Guardar_tiket(matriz, idUsuario, infoPelicula, funcion, sala):
    # Asignar el idUsuario a las sillas seleccionadas ('S')
    sillas_seleccionadas = []
    for i, v in enumerate(matriz):
        for j, v2 in enumerate(v):
            if v2 == idUsuario:
                sillas_seleccionadas.append((i, j))
            elif v2 == "S":
                sillas_seleccionadas.append((i, j))
                matriz[i][j] = idUsuario

    # Función para seleccionar la ruta de guardado del archivo
    def seleccionar_ruta_guardado():
        ruta_archivo = filedialog.asksaveasfilename(
            defaultextension=".txt",  # Extensión por defecto
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],  # Tipos de archivos permitidos
            title="Guardar tiquete como"  # Título del diálogo
        )
        if ruta_archivo:
            with open(ruta_archivo, 'w') as file:
                file.write(f"Película: {infoPelicula['nombre']}\n")
                file.write(f"Sala: {sala['nombre']}\n")
                file.write(f"Fecha: {funcion['fecha']}\n")
                file.write(f"Duración: {infoPelicula['dura']}H\n")
                file.write("Sillas seleccionadas:\n")
                for silla in sillas_seleccionadas:
                    file.write(f"Silla {silla[0]}-{silla[1]}\n")
    
    # Llamar a la función para seleccionar la ruta de guardado
    seleccionar_ruta_guardado()

    # Mostrar mensaje de confirmación
    infoUser = GetUserId(idUsuario)

    from hooks.Peticiones.apdate.updateSillas import updateSillas
    updateSillas(id=funcion["id"], sillas=matriz, idUsuario=idUsuario)

    messagebox.showinfo("Guardado", "El tiquete se guardó con éxito")

    # Redirigir al índice después de guardar el tiquete
    index = Index(ventana=infoPelicula["ventana"], infoUser=infoUser)
