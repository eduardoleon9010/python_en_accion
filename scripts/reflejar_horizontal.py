# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:08:30 2024

@author: USUARIO
"""

from PIL import Image

def reflejar_horizontal(imagen_path):
    """Refleja horizontalmente una imagen cuadrada.
    
    Args:
        imagen_path (str): Ruta de la imagen a reflejar.
        
    Returns:
        PIL.Image: Imagen reflejada horizontalmente.
    """
    imagen = Image.open(imagen_path)
    imagen_reflejada = imagen.transpose(Image.FLIP_LEFT_RIGHT)
    return imagen_reflejada

# Ruta de la imagen "muestra.jpg"
imagen_path = "muestra.jpg"

# Reflejar horizontalmente la imagen
imagen_reflejada = reflejar_horizontal(imagen_path)

# Mostrar la imagen original y la imagen reflejada
imagen_reflejada.show()

