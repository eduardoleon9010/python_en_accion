# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:09:01 2024

@author: USUARIO
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def mostrar_imagen(ruta_imagen: str) -> None:
    """Muestra la imagen ubicada en la ruta especificada.

    Parámetros:
    ruta_imagen (str): La ruta de la imagen que se desea mostrar.

    Retorno:
    None
    """
    # Cargar la imagen desde la ruta especificada
    imagen = mpimg.imread(ruta_imagen)

    # Mostrar la imagen
    plt.imshow(imagen)
    plt.axis('off')  # Desactivar ejes para una mejor visualización
    plt.show()

# Ejemplo de uso
mostrar_imagen("muestra.jpg")
