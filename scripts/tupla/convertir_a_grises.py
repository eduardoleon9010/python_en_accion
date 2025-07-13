# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:23:40 2024

@author: USUARIO
"""

from PIL import Image

def convertir_a_grises(imagen: list) -> None:
    """
    Convierte una imagen en formato RGB a una imagen en escala de grises.

    Args:
        imagen (list): La imagen representada como una lista de listas de tuplas, donde cada tupla contiene
        los valores de rojo, verde y azul de un píxel.

    Returns:
        None
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    for i in range(0, alto):
        for j in range(0, ancho):
            rojo, verde, azul = imagen[i][j]
            gris = (rojo + verde + azul) // 3
            imagen[i][j] = (gris, gris, gris)

def cargar_imagen(ruta: str) -> list:
    """
    Carga una imagen desde la ruta especificada.

    Args:
        ruta (str): La ruta de la imagen a cargar.

    Returns:
        list: La imagen representada como una lista de listas de tuplas, donde cada tupla contiene
        los valores de rojo, verde y azul de un píxel.
    """
    imagen = Image.open(ruta)
    imagen_rgb = imagen.convert('RGB')
    ancho, alto = imagen.size
    imagen_lista = [[imagen_rgb.getpixel((x, y)) for x in range(ancho)] for y in range(alto)]
    return imagen_lista

# Cargar la imagen 'muestra.jpg'
imagen_original = cargar_imagen('muestra.jpg')

# Convertir la imagen a escala de grises
convertir_a_grises(imagen_original)

# Guardar y mostrar la imagen en escala de grises
imagen_gris = Image.new('RGB', (len(imagen_original[0]), len(imagen_original)))
for y, fila in enumerate(imagen_original):
    for x, pixel in enumerate(fila):
        imagen_gris.putpixel((x, y), pixel)
imagen_gris.show()
