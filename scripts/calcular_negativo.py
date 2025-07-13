# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:57:32 2024

@author: USUARIO
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def calcular_negativo(imagen: list) -> list:
    """ Calcula el negativo de una imagen.
    
    Esta función toma una imagen representada como una matriz de píxeles, donde cada píxel
    está representado por una tupla de tres valores (R, G, B) que indican los componentes
    de color rojo, verde y azul, respectivamente. Luego, calcula el negativo de la imagen
    invirtiendo los valores de cada componente de color en cada píxel de la imagen.
    
    Parámetros:
        imagen (list): Matriz de MxN con tuplas (R, G, B) que representan la imagen.
        
    Retorno:
        list: Matriz de MxN con tuplas (R', G', B') que representan el negativo de la imagen.
    """
    negativo = []
    for fila in imagen:
        fila_negativa = []
        for pixel in fila:
            # Calcula el negativo de cada componente de color (R, G, B)
            r_negativo = 255 - pixel[0]
            g_negativo = 255 - pixel[1]
            b_negativo = 255 - pixel[2]
            # Agrega el nuevo pixel al negativo de la imagen
            fila_negativa.append((r_negativo, g_negativo, b_negativo))
        negativo.append(fila_negativa)
    return negativo

def visualizar_imagen(imagen: list) -> None:
    """ Muestra la imagen recibida.
    
    Parámetros:
        imagen (list): Matriz de MxN con tuplas (R, G, B) que representan la imagen a visualizar.
        
    Retorno:
        None
    """
    plt.imshow(imagen)
    plt.axis('off')
    plt.show()

# Ejemplo de uso
imagen_original = mpimg.imread("muestra.jpg").tolist()
imagen_negativa = calcular_negativo(imagen_original)
visualizar_imagen(imagen_negativa)
