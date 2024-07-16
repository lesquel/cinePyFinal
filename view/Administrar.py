def Administrar(ventana, infoUser):
    import customtkinter as ctk
    from datos.UrlImgs import UrlIcos
    from layout import Layout
    from components.Nav import NavAdmid
    from components.administrar.infoAdministrar import infoAdministrar
    
    # Crear el marco principal
    frame = Layout(ventana=ventana)
    # Añadir el menú lateral
    NavAdmid(frame, [
        {"ventana": ventana, "infoUser": infoUser},
    ])

    from datos.peliculas import peliculas as infoPeliculas
    from datos.salas import salsas as infoSalas
    from datos.funciones import funciones as infoFunciones

    peliculas = infoAdministrar(frame, ventana=ventana, infoUser=infoUser, infoFrame={"nombre": "Peliculas", "img": UrlIcos["funciones"], "row": 0, "column": 1}, infoDato=infoPeliculas)
    salas = infoAdministrar(frame, ventana=ventana, infoUser=infoUser, infoFrame={"nombre": "Salas", "img": UrlIcos["salas"], "row": 0, "column": 2}, infoDato=infoSalas)
    funciones = infoAdministrar(frame, ventana=ventana, infoUser=infoUser, infoFrame={"nombre": "Funciones", "img": UrlIcos["movie"],  "row": 0, "column": 3}, infoDato=infoFunciones)
    return frame
    