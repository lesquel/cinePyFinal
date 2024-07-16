def registrar(registro_ventana, datosEntry):
    nombre = datosEntry[0].get()
    img = datosEntry[1].get()
    edad = datosEntry[2].get()
    usuario = datosEntry[3].get()
    correo = datosEntry[4].get()
    contrasena = datosEntry[5].get()    

    from datos.perfil import perfil
    perfil.append({
        "id": len(perfil) + 1,
        "name": nombre,
        "img": img,
        "edad": edad,
        "nombre": usuario,
        "correo": correo,
        "contra": contrasena
    })
    
    # Mostrar un mensaje de éxito
    from tkinter import messagebox
    messagebox.showinfo("Registro exitoso", "Tus datos han sido registrados con éxito.")
    registro_ventana.destroy()
