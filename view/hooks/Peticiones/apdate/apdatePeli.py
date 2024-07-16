import requests
def apdatePeli(infoPelicula, infoUser, ventana):
    from tkinter import messagebox
    print(f"Actualizar película: {infoPelicula}")
    # Realizar la solicitud PUT para actualizar la información de la película
    # http://localhost:8080/updatePelicula?id=1&nombre=1&img=1&descri=1&dura=1&trailers=1&genero_id=1
    url = f"http://localhost:8080/updatePelicula?id={infoPelicula['id']}&nombre={infoPelicula['nombre']}&img={infoPelicula['img']}&descri={infoPelicula['descri']}&dura={infoPelicula['dura']}&trailers={infoPelicula['trailers']}&genero_id={infoPelicula['genero_id']}"
    response = requests.get(url)
    messagebox.showinfo("Actualizar", "La actualización se realizo con éxito")
    from index import Index
    Index(ventana=ventana, infoUser=infoUser, ifAdmin=True)
    return 