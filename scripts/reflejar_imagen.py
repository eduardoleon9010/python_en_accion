# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 23:04:44 2024

@author: USUARIO
"""

def reflejar_imagen(imagen: list) -> list:
    """
    Refleja verticalmente una imagen sobre una línea imaginaria en el centro de la figura, creando una imagen espejo de la figura original.

    Args:
    imagen (list): Matriz que representa la imagen, donde cada elemento es una tupla de 3 flotantes entre 0 y 1
                   representando los valores R, G y B del píxel.

    Returns:
    list: Matriz que representa la imagen reflejada, donde se intercambian las columnas de píxeles de la imagen original.
    """
    num_columnas = len(imagen[0])
    imagen_reflejada = []
    for fila in imagen:
        fila_reflejada = []
        for i in range(num_columnas - 1, -1, -1):
            fila_reflejada.append(fila[i])
        imagen_reflejada.append(fila_reflejada)
    return imagen_reflejada

# Definimos una imagen de ejemplo como una matriz de píxeles representados por tuplas (R, G, B)
imagen_original = [
    [(0.2, 0.4, 0.6), (0.1, 0.2, 0.3), (0.5, 0.6, 0.7)],
    [(0.7, 0.2, 0.9), (0.3, 0.8, 0.2), (0.6, 0.1, 0.4)],
    [(0.4, 0.5, 0.1), (0.9, 0.3, 0.2), (0.8, 0.7, 0.6)]
]

# Mostramos la imagen original
print("Imagen original:")
for fila in imagen_original:
    print(fila)

# Reflejamos la imagen original verticalmente
imagen_reflejada = reflejar_imagen(imagen_original)

# Mostramos la imagen reflejada
print("\nImagen reflejada:")
for fila in imagen_reflejada:
    print(fila)
