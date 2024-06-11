def Recomendado(matriz):
    # Dimensiones de la matriz
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Calcular las columnas centrales
    centro_izquierda = (columnas // 2) - 1
    centro_derecha = columnas // 2

    # Lista de columnas para recorrer, empezando por el centro y moviéndose hacia los extremos
    columnas_ordenadas = list(range(centro_derecha, columnas)) + list(range(centro_izquierda, -1, -1))
    
    for i in range(filas):
        for j in columnas_ordenadas:
            if matriz[i][j] == 'R':
                return matriz

    # Recorrer la matriz comenzando por el centro y desde la última fila hacia la primera
    for i in range(filas-1, -1, -1):
        for j in columnas_ordenadas:
            if matriz[i][j] == 'L':
                matriz[i][j] = 'R'
                return matriz  # Salir de la función después de marcar la primera 'L'
    
    return matriz