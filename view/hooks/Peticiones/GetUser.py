def GetUser(usuario, contrasena):
    from datos.perfil import perfil
    buscarNombreContra = lambda nombre, contra: next((perfil for perfil in perfil if perfil["nombre"] == nombre and perfil["contra"] == contra), None)
    return buscarNombreContra(nombre=usuario, contra=contrasena)
def GetUserId(idUsuario):
    from datos.perfil import perfil
    buscarId = lambda id: next((perfil for perfil in perfil if perfil["id"] == id), None)
    return buscarId(id=idUsuario)