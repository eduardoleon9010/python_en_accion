# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:49:52 2024

@author: USUARIO
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def rotar_izquierda(imagen: np.ndarray) -> np.ndarray:
    """Rota una imagen cuadrada 90 grados a la izquierda.

    Args:
        imagen (np.ndarray): La imagen representada como un array numpy.

    Returns:
        np.ndarray: La imagen rotada 90 grados a la izquierda.
    """
    # Transpone la imagen para intercambiar filas y columnas
    imagen_transpuesta = np.transpose(imagen, axes=(1, 0, 2))

    # Invierte el orden de las columnas para rotar 90 grados a la izquierda
    imagen_rotada = np.flip(imagen_transpuesta, axis=0)

    return imagen_rotada


# Carga una imagen cuadrada para probar la rotación
ruta_imagen = "D:/My Backups/Formacion/Big Data/Andes/Python-Andes/M4/tupla/muestra.jpg"
imagen_cuadrada = mpimg.imread(ruta_imagen)

# Realiza la rotación de la imagen
imagen_rotada = rotar_izquierda(imagen_cuadrada)

# Muestra la imagen original y la imagen rotada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(imagen_cuadrada)
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(imagen_rotada)
plt.title("Imagen Rotada a la Izquierda")
plt.axis("off")

plt.show()
