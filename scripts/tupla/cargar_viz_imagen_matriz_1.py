# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:35:04 2024

@author: USUARIO
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def visualizar_imagen(imagen: list) -> None:
    """ 
    Muestra la imagen recibida.

    Args:
        imagen (list): Una matriz de MxN con tuplas (R,G,B) que representan la imagen a visualizar.
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    
    # Construir una matriz para representar la imagen.
    # Esta matriz tendrá tres dimensiones
    matriz = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            # convertir la tupla a una lista
            r, g, b = imagen[i][j]
            fila.append([r, g, b])
        matriz.append(fila)
    plt.imshow(matriz)
    plt.show()

def cargar_imagen() -> list:
    """ 
    Carga la imagen que se encuentra en la ruta dada por el usuario.

    Returns:
        list: Matriz de MxN con tuplas (R,G,B).
    """
    ruta_imagen = input("Ingrese la ruta de la imagen: ")
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

# Ejemplo de uso de las funciones
imagen = cargar_imagen()
visualizar_imagen(imagen)
