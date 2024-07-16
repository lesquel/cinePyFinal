import requests

def insertPelicula(entries, label_imagen, main_frame, ventana, infoUser):
    from components.GeneroEntry import obtener_id_genero
    # Obtener los valores de los campos de entrada
    nombre = entries["nombre"].get()
    genero = obtener_id_genero(entries["genero"].get())
    duracion = entries["duracion"].get()
    trailer = entries["trailer"].get()
    descripcion = entries["descripcion"].get()
    img = entries["img"].get()

    # Imprimir los valores para verificar
    print(f"Nombre: {nombre}, Genero: {genero}, Duracion: {duracion}, Trailer: {trailer}, Descripcion: {descripcion}, Img: {img}")
    
    # Construir la URL de la solicitud GET para insertar la película
    url = f"http://localhost:8080/insertPelicula?nombre={nombre}&genero_id={genero}&dura={duracion}&trailers={trailer}&descri={descripcion}&img={img}"
    # Enviar la solicitud GET
    response = requests.get(url)

    import customtkinter as ctk
    # Borrar los valores de los campos de entrada después de la inserción exitosa
    entries["nombre"].delete(0, ctk.END)
    entries["duracion"].delete(0, ctk.END)
    entries["trailer"].delete(0, ctk.END)
    entries["descripcion"].delete(0, ctk.END)
    entries["img"].delete(0, ctk.END)
    label_imagen.configure(image=None)
    label_imagen.image = None  # Borrar la imagen de la etiqueta

    from tkinter import messagebox
    messagebox.showinfo("Información", "La película se ha insertado correctamente")
    from components.tablaCrud.tablaPelicula import TablaPelicula
    TablaPelicula(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    return response.json()
