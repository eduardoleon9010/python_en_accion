# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:54:09 2024

@author: USUARIO
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def visualizar_imagen(imagen: list) -> None:
    """ Muestra la imagen recibida.
    
    Esta función muestra la imagen representada por la matriz recibida como parámetro.
    
    Parámetros:
        imagen (list): Matriz de MxN con tuplas (R, G, B) que representan la imagen a visualizar.
        
    Retorno:
        None
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    
    # Construir una matriz para representar la imagen.
    # Esta matriz tendrá tres dimensiones
    matriz = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            # Convertir la tupla a una lista
            r, g, b = imagen[i][j]
            fila.append([r, g, b])
        matriz.append(fila)
    plt.imshow(matriz)
    plt.show()


def cargar_imagen(ruta_imagen: str) -> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    
    Parámetros:
        ruta_imagen (str): Ruta donde se encuentra la imagen a cargar.
        
    Retorno:
        list: Matriz de MxN con tuplas (R, G, B).
    """
    matriz = mpimg.imread(ruta_imagen).tolist()
    alto = len(matriz)
    ancho = len(matriz[0])
    
    # Construir una matriz para representar la imagen.
    # Esta matriz tendrá dos dimensiones y tuplas en cada casilla.
    imagen = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            # Extraer los componentes. Note que no se puede desempaquetar.
            r = matriz[i][j][0]
            g = matriz[i][j][1]
            b = matriz[i][j][2]
            
            # Construir la tupla equivalente y agregarla a la imagen
            tupla = (r, g, b)
            fila.append(tupla)
        imagen.append(fila)
    return imagen

# Ejemplo de uso
imagen = cargar_imagen("muestra.jpg")
visualizar_imagen(imagen)
