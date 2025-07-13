# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:49:49 2024

@author: USUARIO
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def cargar_imagen_matriz(ruta_imagen: str) -> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    
    Esta función utiliza la biblioteca `matplotlib.image` para cargar la imagen ubicada en la ruta especificada.
    
    Parámetros:
        ruta_imagen (str): Ruta donde se encuentra la imagen a cargar.
        
    Retorno:
        list: Matriz de MxNx3 que representa la imagen.
            Cada elemento de la matriz corresponde a un píxel de la imagen, representado como una tupla de tres valores (rojo, verde, azul).
            La matriz resultante es de tamaño MxN, donde M es el número de filas y N es el número de columnas de la imagen.
    """
    imagen = mpimg.imread(ruta_imagen)
    return imagen

def visualizar_imagen_matriz(imagen: list) -> None:
    """ Muestra la imagen recibida.
    
    Esta función utiliza la biblioteca `matplotlib.pyplot` para visualizar la imagen representada por la matriz recibida como parámetro.
    
    Parámetros:
        imagen (list): Matriz de MxNx3 que representa la imagen a visualizar.
            Cada elemento de la matriz corresponde a un píxel de la imagen, representado como una tupla de tres valores (rojo, verde, azul).
            La matriz debe ser de tamaño MxN, donde M es el número de filas y N es el número de columnas de la imagen.
            
    Retorno:
        None
    """
    plt.imshow(imagen)
    plt.show()

# Ejemplo de uso
imagen = cargar_imagen_matriz("muestra.jpg")
visualizar_imagen_matriz(imagen)
   