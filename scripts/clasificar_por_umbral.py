# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:03:28 2024

@author: USUARIO
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def cargar_imagen_gris(ruta_imagen: str) -> np.ndarray:
    """Carga la imagen dada en escala de grises.
    
    Args:
        ruta_imagen (str): Ruta de la imagen a cargar.
        
    Returns:
        np.ndarray: Matriz de la imagen en escala de grises.
    """
    imagen = mpimg.imread(ruta_imagen)
    # Convertir la imagen a escala de grises
    imagen_gris = np.dot(imagen[...,:3], [0.2989, 0.5870, 0.1140])
    return imagen_gris

def clasificar_por_umbral(imagen: np.ndarray, umbrales: list) -> np.ndarray:
    """Clasifica los píxeles de la imagen de acuerdo a los umbrales dados.
    
    Args:
        imagen (np.ndarray): Matriz de la imagen en escala de grises.
        umbrales (list): Lista ordenada de umbrales.
        
    Returns:
        np.ndarray: Imagen clasificada.
    """
    # Crear una copia de la imagen
    imagen_clasificada = np.copy(imagen)
    # Aplicar los umbrales
    for i, umbral in enumerate(umbrales):
        # Asignar el valor correspondiente a los píxeles
        imagen_clasificada[imagen >= umbral] = umbral
    return imagen_clasificada

def visualizar_imagen(imagen: np.ndarray) -> None:
    """Visualiza la imagen dada.
    
    Args:
        imagen (np.ndarray): Imagen a visualizar.
    """
    plt.imshow(imagen, cmap='gray')
    plt.axis('off')
    plt.show()

# Cargar la imagen "muestra.jpg" en escala de grises
imagen_gris = cargar_imagen_gris("muestra.jpg")

# Definir los umbrales
umbrales = [50, 100, 150]

# Obtener la imagen clasificada
imagen_clasificada = clasificar_por_umbral(imagen_gris, umbrales)

# Visualizar la imagen clasificada
visualizar_imagen(imagen_clasificada)
