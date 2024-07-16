def GuardarPeli(infoPelicula, newInfoPelicula):
    from tkinter import messagebox
    from datos.peliculas import peliculas
    buscarIdPelicula = lambda idPelicula: next((pelicula for pelicula in peliculas if pelicula["id"] == idPelicula), None)
    pelicula = buscarIdPelicula(idPelicula=infoPelicula["id"])
    pelicula["nombre"] = newInfoPelicula["nombre"]
    pelicula["descri"] = newInfoPelicula["descri"]
    pelicula["dura"] = newInfoPelicula["dura"]
    pelicula["img"] = newInfoPelicula["img"]
    messagebox.showinfo("Guardar", "La película se ha guardado correctamente")