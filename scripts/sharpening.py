# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:44:10 2024

@author: USUARIO
"""

def copiar_imagen(imagen: list) -> list:
    """ Esta función crea una copia de una imagen y la retorna
    Parámetros:
      imagen (list): es una lista de listas de tuplas que representa una imagen.
    Retorno:
      (list): retorna una copia de la imagen
    """
    copia = []
    alto = len(imagen)
    for i in range(0, alto):
        fila = imagen[i]
        nueva_fila = fila.copy()
        copia.append(nueva_fila)
    return copia

def sharpening(imagen: list) -> list:
    """ Aplica la máscara sobre la imagen. La imagen que se 
    recibe como parámetro no se modifica durante el proceso.
    Parámetros:
      imagen (list): La imagen sobre la que se aplicará el algoritmo
    Retorno:
      (list): la imagen con el resultado de aplicar el algoritmo
    """
    # Acá se crea la máscara que se va a aplicar
    mascara = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]
    
    # Crear una copia de la imagen que finalmente será retornada
    copia = copiar_imagen(imagen)
    alto = len(imagen)
    ancho = len(imagen[0])
    
    # Recorrer las filas (i) y las columnas (j) de la imagen original
    # No se recorren las filas y columnas que se encuentran en el borde de 
    # la imagen porque no tienen vecinos completos para aplicar la máscara
    for i in range(1, alto - 1):
        for j in range(1, ancho - 1):
            
            # A partir de este punto se va a aplicar la máscara al pixel que
            # se encuentra en la fila i, columnas j.
            # La máscara es de 3x3: se hacen dos ciclos para recorrer todos sus elementos.
            rojo, verde, azul = (0, 0, 0)
            for i_mascara in range(-1, 2):
                for j_mascara in range(-1, 2):
                    # Se consultan los colores originales del pixel vecino
                    rojo_vecino, verde_vecino, azul_vecino = imagen[i + i_mascara][j + j_mascara]
                    valor_mascara = mascara[i_mascara + 1][j_mascara + 1]
                    
                    # Los colores originales se multiplican por el valor de la máscara
                    # y se van sumando para encontrar el nuevo valor del color para
                    # el pixel [i][j]
                    rojo += rojo_vecino * valor_mascara
                    verde += verde_vecino * valor_mascara
                    azul += azul_vecino * valor_mascara
            
            nuevo_pixel = (max(rojo, 0.0), max(verde, 0.0), max(azul, 0.0))
            copia[i][j] = nuevo_pixel
    return copia

# Ejemplo de uso
imagen_original = [
    [(10, 20, 30), (40, 50, 60), (70, 80, 90)],
    [(100, 110, 120), (130, 140, 150), (160, 170, 180)],
    [(190, 200, 210), (220, 230, 240), (250, 0, 0)]  # Última fila con un color fuera de rango
]

# Se crea una copia de la imagen original
imagen_copia = copiar_imagen(imagen_original)

# Se aplica el sharpening a la imagen copiada
imagen_sharpened = sharpening(imagen_copia)

# Visualizar los resultados o realizar más operaciones según sea necesario
print("Imagen original:", imagen_original)
print("Imagen copiada:", imagen_copia)
print("Imagen después de aplicar sharpening:", imagen_sharpened)
