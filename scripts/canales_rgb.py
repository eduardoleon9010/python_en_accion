# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:00:43 2024

@author: USUARIO
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def canales_rgb(imagen: list) -> list:
    """ Divide una imagen en sus canales de color rojo, verde y azul.
    
    Esta función divide una imagen en sus canales de color rojo, verde y azul.
    Cada canal se almacena en una imagen separada donde la intensidad de cada
    píxel corresponde a la intensidad del color en ese canal en la imagen original.
    
    Parámetros:
        imagen (list): Matriz de MxN con tuplas (R, G, B) que representan la imagen original.
        
    Retorno:
        list: Lista de tres imágenes, cada una representando un canal de color (rojo, verde, azul).
    """
    alto, ancho = len(imagen), len(imagen[0])
    
    # Inicializar matrices para los canales rojo, verde y azul
    canal_rojo = np.zeros((alto, ancho, 3), dtype=np.uint8)
    canal_verde = np.zeros((alto, ancho, 3), dtype=np.uint8)
    canal_azul = np.zeros((alto, ancho, 3), dtype=np.uint8)
    
    # Recorrer la imagen y asignar los valores correspondientes a cada canal
    for i in range(alto):
        for j in range(ancho):
            r, g, b = imagen[i][j]
            # Canal Rojo: r, 0, 0
            canal_rojo[i][j] = [r, 0, 0]
            # Canal Verde: 0, g, 0
            canal_verde[i][j] = [0, g, 0]
            # Canal Azul: 0, 0, b
            canal_azul[i][j] = [0, 0, b]
    
    return [canal_rojo, canal_verde, canal_azul]

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
canales = canales_rgb(imagen_original)

# Visualizar los canales
for i, canal in enumerate(canales):
    print(f"Canal {i+1}")
    visualizar_imagen(canal)
