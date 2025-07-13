# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:21:08 2024

@author: USUARIO
"""

import random
import matplotlib.pyplot as plt

def generar_imagen_tuplas(ancho: int) -> list:
    """
    Genera una imagen representada como una lista de listas de tuplas, donde cada tupla contiene los valores
    de rojo, verde y azul de un píxel generado aleatoriamente.

    Args:
        ancho (int): El ancho de la imagen (número de píxeles).

    Returns:
        list: Una lista que representa la imagen, donde cada elemento de la lista representa una fila de la imagen,
        y cada fila contiene una lista de tuplas que representan los píxeles. Cada tupla tiene tres valores: (rojo, verde, azul),
        que van de 0 a 255 (valores enteros) representando la intensidad de cada color.
    """
    imagen = []
    for i in range(0, ancho):
        fila = []
        for j in range(0, ancho):
            rojo = random.randint(0, i) / ancho
            verde = random.randint(0, j) / ancho
            azul = max(0, 1 - rojo - verde)
            pixel = (int(rojo * 255), int(verde * 255), int(azul * 255))
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


# Ejemplo de uso de la función generar_imagen_tuplas y visualizar_imagen
ancho_imagen = 100
imagen_tuplas = generar_imagen_tuplas(ancho_imagen)
visualizar_imagen(imagen_tuplas)
