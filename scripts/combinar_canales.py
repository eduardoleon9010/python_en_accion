# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:01:41 2024

@author: USUARIO
"""
import numpy as np
import matplotlib.pyplot as plt

def combinar_canales(canal_rojo: list, canal_verde: list, canal_azul: list) -> list:
    """ Combina tres imágenes en escala de grises correspondientes a los canales rojo, verde y azul de una imagen.
    
    Esta función toma tres imágenes en escala de grises correspondientes a los canales rojo, verde y azul de una imagen,
    y produce una imagen combinada. Este proceso es similar al utilizado por Sergey Prokudin-Gorsky para producir fotografías
    en color a partir de fotografías en blanco y negro tomadas con filtros de colores.
    
    Parámetros:
        canal_rojo (list): Matriz de MxN con valores de intensidad en escala de grises correspondientes al canal rojo.
        canal_verde (list): Matriz de MxN con valores de intensidad en escala de grises correspondientes al canal verde.
        canal_azul (list): Matriz de MxN con valores de intensidad en escala de grises correspondientes al canal azul.
        
    Retorno:
        list: Matriz de MxN con tuplas (R, G, B) que representan la imagen combinada.
    """
    # Convertir las matrices en arrays de NumPy
    canal_rojo = np.array(canal_rojo)
    canal_verde = np.array(canal_verde)
    canal_azul = np.array(canal_azul)
    
    # Combinar los canales en una sola imagen
    imagen_combinada = np.dstack((canal_rojo, canal_verde, canal_azul))
    
    return imagen_combinada

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
# Suponiendo que tienes tres imágenes en escala de grises correspondientes a los canales rojo, verde y azul
# llamadas canal_rojo, canal_verde y canal_azul respectivamente

# Crear las imágenes de ejemplo (reemplaza estos con tus imágenes reales)
canal_rojo = [[100, 150], [120, 180]]  # Ejemplo de canal rojo
canal_verde = [[50, 80], [70, 100]]  # Ejemplo de canal verde
canal_azul = [[200, 220], [210, 240]]  # Ejemplo de canal azul

# Combinar los canales en una sola imagen
imagen_combinada = combinar_canales(canal_rojo, canal_verde, canal_azul)

# Visualizar la imagen combinada
visualizar_imagen(imagen_combinada)
