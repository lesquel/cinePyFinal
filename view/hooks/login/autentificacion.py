from tkinter import messagebox
def autentificacion(ventana, usuario, contrasena):
    if usuario == "":
        messagebox.showinfo("Error", "Introduzca el usuario")
        return
    if contrasena == "":
        messagebox.showinfo("Error", "Introduzca la contraseña")
        return
    from hooks.Peticiones.GetUser import GetUser
    infoUser = GetUser(usuario, contrasena)

    from index import Index 
    if not infoUser:
        messagebox.showinfo("Error", "Usuario o contraseña incorrectos")
    if "admin" not in infoUser or infoUser["admin"] == False:
        return Index(ventana, infoUser=infoUser)
    else:
        return Index(ventana, infoUser=infoUser, ifAdmin=True)