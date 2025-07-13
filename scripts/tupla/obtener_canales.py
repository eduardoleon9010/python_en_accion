# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:42:00 2024

@author: USUARIO
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def obtener_canales(imagen: np.ndarray) -> tuple:
    """Obtiene los canales Rojo, Verde y Azul de una imagen.

    Args:
        imagen (np.ndarray): La imagen representada como un array numpy.

    Returns:
        tuple: Una tupla que contiene tres imágenes en escala de grises correspondientes a los canales Rojo, Verde y Azul de la imagen original.
    """
    # Extrae los canales de la imagen original
    canal_rojo = imagen[:, :, 0]
    canal_verde = imagen[:, :, 1]
    canal_azul = imagen[:, :, 2]

    return canal_rojo, canal_verde, canal_azul


# Carga la imagen
imagen = mpimg.imread("muestra.jpg")

# Obtiene los canales Rojo, Verde y Azul de la imagen
canal_rojo, canal_verde, canal_azul = obtener_canales(imagen)

# Muestra las imágenes de los canales
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(canal_rojo, cmap='gray')
plt.title("Canal Rojo")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(canal_verde, cmap='gray')
plt.title("Canal Verde")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(canal_azul, cmap='gray')
plt.title("Canal Azul")
plt.axis("off")

plt.show()
