# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 22:13:39 2024

@author: USUARIO
"""

def binarizar_imagen(imagen: list, umbral: float) -> list:
    """
    Binariza una imagen representada como una matriz, cambiando los píxeles con valores de color iguales o mayores
    al umbral a blanco y los píxeles con valores de color por debajo del umbral a negro.

    Args:
    imagen (list): Matriz que representa la imagen, donde cada elemento es una tupla de 3 flotantes entre 0 y 1
                   representando los valores R, G y B del píxel.
    umbral (float): Umbral de binarización, valor entre 0 y 1.

    Returns:
    list: Matriz que representa la imagen binarizada, donde cada píxel se representa como una tupla de 3 flotantes
          con valores 0 o 1, donde 0 representa negro y 1 representa blanco.
    """
    # Inicializamos la matriz para la imagen binarizada
    imagen_binarizada = []

    # Iteramos sobre cada fila de la imagen
    for fila in imagen:
        # Inicializamos una lista para almacenar los píxeles binarizados de la fila
        fila_binarizada = []

        # Iteramos sobre cada píxel en la fila
        for pixel in fila:
            # Calculamos el promedio de los valores R, G y B del píxel
            promedio_color = sum(pixel) / 3

            # Si el promedio es mayor o igual al umbral, el píxel se cambia a blanco (todos los valores 1)
            # De lo contrario, el píxel se cambia a negro (todos los valores 0)
            if promedio_color >= umbral:
                pixel_binarizado = (1, 1, 1)  # Blanco
            else:
                pixel_binarizado = (0, 0, 0)  # Negro

            # Agregamos el píxel binarizado a la fila binarizada
            fila_binarizada.append(pixel_binarizado)

        # Agregamos la fila binarizada a la imagen binarizada
        imagen_binarizada.append(fila_binarizada)

    return imagen_binarizada

# Definimos una imagen de ejemplo como una matriz de píxeles representados por tuplas (R, G, B)
imagen_original = [
    [(0.2, 0.4, 0.6), (0.7, 0.1, 0.9), (0.5, 0.8, 0.2)],
    [(0.8, 0.3, 0.4), (0.2, 0.6, 0.5), (0.9, 0.7, 0.1)],
    [(0.1, 0.5, 0.3), (0.4, 0.7, 0.9), (0.6, 0.2, 0.8)]
]

# Especificamos el umbral de binarización
umbral = 0.5

# Binarizamos la imagen original
imagen_binarizada = binarizar_imagen(imagen_original, umbral)

# Mostramos la imagen binarizada
print("Imagen binarizada:")
for fila in imagen_binarizada:
    print(fila)
