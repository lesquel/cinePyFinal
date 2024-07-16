import requests
def GetComentarios(idPelicula):
    res = requests.get(f"http://localhost:8080/getComentario?idPelicula={idPelicula}")
    return res.json()
    # from datos.comentarios_peli import comentarios_peli
    # return [comentario for comentario in comentarios_peli if comentario["id_pelicula"] == idPelicula]