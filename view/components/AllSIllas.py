from .Sillas import Sillas
import hooks.Cambiar_Guardar as Cambiar_Guardar

def AllSIllas(matriz, frame, idUsuario):
    def ejecutar2(b, r, c):
        # Usamos `nonlocal` para indicar que `matriz` no es una variable local a `ejecutar2`
        nonlocal matriz
        matriz = Cambiar_Guardar.Cambiar_Guardar(b=b, r=r, c=c, matriz=matriz)
        # Eliminar todos los widgets hijos en el frame para poder re-renderizar

    # Crear los botones para la matriz de sillas
    for i, f in enumerate(matriz):
        for j, c in enumerate(f):
            if c == "L":
                b, r, c = Sillas(parent=frame, texto=c, tamanio=16, row=i, column=j, bg_color="#8888ff")
                b.configure(command=lambda b=b, r=i, c=j: ejecutar2(b, r, c))
            elif c == "S":
                Sillas(parent=frame, texto=c, tamanio=16, row=i, column=j, bg_color="#888888")
            elif c == "R":
                b, r, c = Sillas(parent=frame, texto=c, tamanio=16, row=i, column=j, bg_color="#88ff88")
                b.configure(command=lambda b=b, r=i, c=j: ejecutar2(b, r, c))
            elif c == idUsuario:
                b, r, c = Sillas(parent=frame, texto="M", tamanio=16, row=i, column=j, bg_color="#ffff00")
                b.configure(command=lambda b=b, r=i, c=j: ejecutar2(b, r, c))
            else:  # Asientos ocupados por otros usuarios
                Sillas(parent=frame, texto="O", tamanio=16, row=i, column=j, bg_color="#ff8888")
