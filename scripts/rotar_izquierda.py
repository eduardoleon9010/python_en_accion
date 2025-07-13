# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:07:53 2024

@author: USUARIO
"""

from PIL import Image

def rotar_izquierda(imagen_path):
    """Rota a la izquierda una imagen cuadrada.
    
    Args:
        imagen_path (str): Ruta de la imagen a rotar.
        
    Returns:
        PIL.Image: Imagen rotada a la izquierda.
    """
    imagen = Image.open(imagen_path)
    imagen_rotada = imagen.transpose(Image.ROTATE_90)
    return imagen_rotada

# Ruta de la imagen "muestra.jpg"
imagen_path = "muestra.jpg"

# Rotar la imagen a la izquierda
imagen_rotada = rotar_izquierda(imagen_path)

# Mostrar la imagen original y la imagen rotada
imagen_rotada.show()

