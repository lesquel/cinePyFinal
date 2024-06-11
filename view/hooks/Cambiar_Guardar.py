def Cambiar_Guardar(b, r, c, matriz):
    if matriz[r][c] == 'L':
        matriz[r][c] = 'S'
        b.configure(fg_color="#888888", text='S')
    elif matriz[r][c] == 'S':
        matriz[r][c] = 'L'
        b.configure(fg_color="#8888ff", text='L')
    elif matriz[r][c] == 'R':
        matriz[r][c] = 'S'
        b.configure(fg_color="#888888", text='S')
    return matriz
