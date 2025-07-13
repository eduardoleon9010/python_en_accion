# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:07:16 2024

@author: USUARIO
"""

import matplotlib.pyplot as plt

def generar_imagen_negra(ancho: int) -> list:
    """
    Genera una imagen completamente negra representada como una lista de listas de tuplas.
    
    Args:
        ancho (int): El ancho de la imagen (número de píxeles).

    Returns:
        list: Una lista que representa la imagen negra, donde cada elemento de la lista representa una fila de la imagen,
        y cada fila contiene una lista de tuplas que representan los píxeles. Cada tupla tiene tres valores: (rojo, verde, azul),
        que van desde 0.0 (sin color) a 1.0 (color completo).
    """
    imagen = []
    for i in range(0, ancho):
        fila = []
        for j in range(0, ancho):
            rojo = 0.0
            verde = 0.0
            azul = 0.0
            pixel = (rojo, verde, azul)
            fila.append(pixel)
        imagen.append(fila)
    return imagen

def visualizar_imagen(imagen: list):
    """
    Visualiza la imagen generada utilizando la biblioteca matplotlib.

    Args:
        imagen (list): La imagen representada como una lista de listas de tuplas.
    """
    plt.imshow(imagen)
    plt.axis('off')  # Deshabilita los ejes
    plt.show()


# Ejemplo de uso de la función generar_imagen_negra y visualizar_imagen
ancho_imagen = 3
imagen_negra = generar_imagen_negra(ancho_imagen)
visualizar_imagen(imagen_negra)

