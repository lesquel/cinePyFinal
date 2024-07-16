import requests

def insertComentario(idPelicula, comentario, parent, idUsuario):
    url = f"http://localhost:8080/insertComentario?idPelicula={idPelicula}&comentario={comentario}&idUsuario={idUsuario}"
    response = requests.get(url)
    print(response.text)
    from components.Comentarios import Comentarios
    Comentarios(parent=parent, idPelicula=idPelicula, idUsuario=idUsuario)