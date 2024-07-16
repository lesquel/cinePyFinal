def destuirTodo(ventana):
    for child in ventana.winfo_children():
        child.destroy()