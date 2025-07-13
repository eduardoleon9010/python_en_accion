# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:43:39 2024

@author: USUARIO
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def convertir_a_grises(imagen: np.ndarray) -> np.ndarray:
    """Convierte una imagen a escala de grises.

    Args:
        imagen (np.ndarray): La imagen representada como un array numpy.

    Returns:
        np.ndarray: La imagen convertida a escala de grises.
    """
    # Calcula el promedio de los componentes RGB para cada píxel
    return np.mean(imagen, axis=2)


def clasificar_pixeles(imagen: np.ndarray, umbrales: list) -> np.ndarray:
    """Clasifica los píxeles de una imagen de acuerdo a una lista de umbrales.

    Args:
        imagen (np.ndarray): La imagen representada como un array numpy.
        umbrales (list): Una lista ordenada de umbrales.

    Returns:
        np.ndarray: La imagen clasificada según los umbrales especificados.
    """
    # Crea una copia de la imagen original
    imagen_clasificada = np.copy(imagen)

    # Recorre cada píxel de la imagen
    for i in range(imagen.shape[0]):
        for j in range(imagen.shape[1]):
            # Obtiene la intensidad del píxel actual
            intensidad = imagen[i, j]

            # Encuentra el rango de umbral al que pertenece la intensidad
            for k, umbral in enumerate(umbrales):
                if k == 0:
                    if intensidad < umbral:
                        imagen_clasificada[i, j] = 0
                        break
                elif k == len(umbrales) - 1:
                    if intensidad >= umbral:
                        imagen_clasificada[i, j] = 255
                        break
                else:
                    if intensidad >= umbrales[k - 1] and intensidad < umbral:
                        # Calcula el valor de gris en función del umbral actual y el anterior
                        gris = (umbral + umbrales[k - 1]) // 2
                        imagen_clasificada[i, j] = gris
                        break

    return imagen_clasificada


# Carga la imagen
ruta_imagen = "D:/My Backups/Formacion/Big Data/Andes/Python-Andes/M4/tupla/muestra.jpg"
imagen_color = mpimg.imread(ruta_imagen)

# Convierte la imagen a escala de grises
imagen_gris = convertir_a_grises(imagen_color)

# Define los umbrales
umbrales = [50, 100, 150]

# Clasifica los píxeles de la imagen según los umbrales especificados
imagen_clasificada = clasificar_pixeles(imagen_gris, umbrales)

# Muestra la imagen clasificada
plt.imshow(imagen_clasificada, cmap='gray')
plt.axis("off")
plt.title("Imagen Clasificada")
plt.show()

