# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:33:27 2024

@author: USUARIO
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def cargar_imagen_matriz(ruta_imagen: str) -> list:
    """ 
    Carga la imagen que se encuentra en la ruta dada.

    Args:
        ruta_imagen (str): La ruta donde se encuentra la imagen a cargar.

    Returns:
        list: Una matriz de MxNx3 que representa la imagen.
    """
    imagen = mpimg.imread(ruta_imagen)
    return imagen

def visualizar_imagen_matriz(imagen: list) -> None:
    """ 
    Muestra la imagen recibida.

    Args:
        imagen (list): Una matriz de MxNx3 que representa la imagen a visualizar.
    """
    plt.imshow(imagen)
    plt.show()

# Ejemplo de uso de las funciones
imagen = cargar_imagen_matriz("muestra.jpg")
visualizar_imagen_matriz(imagen)
