def GetPeliId(idPelicula):
    from datos.peliculas import peliculas
    buscarIdPelicula = lambda idPelicula: next((pelicula for pelicula in peliculas if pelicula["id"] == idPelicula), None)
    infoPelicula = buscarIdPelicula(idPelicula=idPelicula)
    return infoPelicula