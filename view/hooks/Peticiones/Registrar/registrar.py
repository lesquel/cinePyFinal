def registrar(main_frame, datosEntry):
    nombre = datosEntry[0].get()
    img = datosEntry[1].get()
    edad = datosEntry[2].get()
    usuario = datosEntry[3].get()
    correo = datosEntry[4].get()
    contrasena = datosEntry[5].get()    

    from hooks.Peticiones.insert.insertUser import insertUser

    insertUser(nombre=nombre, img=img, edad=edad, usuario=usuario, correo=correo, contrasena=contrasena)
    
    # Mostrar un mensaje de éxito
    from tkinter import messagebox
    messagebox.showinfo("Registro exitoso", "Tus datos han sido registrados con éxito.")
    main_frame.destroy()
