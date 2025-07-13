# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:59:15 2024

@author: USUARIO
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def convolucion(imagen: list, mascara: list) -> list:
    """ Realiza la convolución entre una imagen y una máscara.
    
    Esta función realiza la convolución entre una imagen y una máscara dada. La convolución
    se realiza sumando los productos de los elementos de la máscara con los píxeles 
    correspondientes en la imagen.
    
    Parámetros:
        imagen (list): Matriz de MxN con tuplas (R, G, B) que representan la imagen.
        mascara (list): Matriz cuadrada de NxN que representa la máscara de convolución.
        
    Retorno:
        list: Matriz de MxN con tuplas (R, G, B) que representa la imagen resultante de la convolución.
    """
    alto, ancho = len(imagen), len(imagen[0])
    tamano_mascara = len(mascara)
    mitad = tamano_mascara // 2
    
    # Crear una copia de la imagen que finalmente será retornada
    imagen_resultado = [fila[:] for fila in imagen]
    
    for i in range(mitad, alto - mitad):
        for j in range(mitad, ancho - mitad):
            nuevo_pixel = [0, 0, 0]
            for k in range(-mitad, mitad + 1):
                for l in range(-mitad, mitad + 1):
                    r, g, b = imagen[i + k][j + l]
                    valor_mascara = mascara[k + mitad][l + mitad]
                    nuevo_pixel[0] += r * valor_mascara
                    nuevo_pixel[1] += g * valor_mascara
                    nuevo_pixel[2] += b * valor_mascara
            
            # Normalizar el nuevo pixel si la suma de la máscara no es 1
            suma_mascara = np.sum(mascara)
            if suma_mascara != 0:
                nuevo_pixel[0] = max(0, min(255, nuevo_pixel[0] / suma_mascara))
                nuevo_pixel[1] = max(0, min(255, nuevo_pixel[1] / suma_mascara))
                nuevo_pixel[2] = max(0, min(255, nuevo_pixel[2] / suma_mascara))
            
            imagen_resultado[i][j] = tuple(map(int, nuevo_pixel))
    
    return imagen_resultado

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
# Definir una máscara de convolución (por ejemplo)
mascara = [[-1, -1, -1],
           [-1,  8, -1],
           [-1, -1, -1]]
imagen_convolucionada = convolucion(imagen_original, mascara)
visualizar_imagen(imagen_convolucionada)
