# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:06:01 2024

@author: USUARIO
"""
from PIL import Image

def rotar_derecha(imagen_path):
    """Rota a la derecha una imagen cuadrada.
    
    Args:
        imagen_path (str): Ruta de la imagen a rotar.
        
    Returns:
        PIL.Image: Imagen rotada a la derecha.
    """
    imagen = Image.open(imagen_path)
    imagen_rotada = imagen.transpose(Image.ROTATE_270)
    return imagen_rotada

# Ruta de la imagen "muestra.jpg"
imagen_path = "muestra.jpg"

# Rotar la imagen a la derecha
imagen_rotada = rotar_derecha(imagen_path)

# Mostrar la imagen original y la imagen rotada
imagen_rotada.show()
