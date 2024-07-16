from datos.UrlImgs import UrlImgs
def Cambiar_Guardar(b, r, c, matriz):
    if matriz[r][c] == 'L':
        matriz[r][c] = 'S'
    elif matriz[r][c] == 'S':
        matriz[r][c] = 'L'
    elif matriz[r][c] == 'R':
        matriz[r][c] = 'S'
    return matriz
