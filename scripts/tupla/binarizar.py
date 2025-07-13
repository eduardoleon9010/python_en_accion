# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:28:31 2024

@author: USUARIO
"""

from PIL import Image

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

def binarizar(imagen: list, umbral: int) -> None:
    """
    Binariza una imagen en escala de grises utilizando un umbral dado.

    Args:
        imagen (list): La imagen representada como una lista de listas de tuplas, donde cada tupla contiene
        los valores de rojo, verde y azul de un píxel en escala de grises.
        umbral (int): El umbral utilizado para binarizar la imagen. Los píxeles con intensidad menor al umbral
        se convierten en negro, mientras que los píxeles con intensidad igual o mayor al umbral se convierten en blanco.

    Returns:
        None
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    for i in range(0, alto):
        for j in range(0, ancho):
            rojo, verde, azul = imagen[i][j]
            gris = (rojo + verde + azul) // 3
            if gris < umbral:
                imagen[i][j] = (0, 0, 0)  # Negro
            else:
                imagen[i][j] = (255, 255, 255)  # Blanco

# Solicitar al usuario que ingrese la ruta de la imagen
ruta_imagen = input("Ingrese la ruta de la imagen: ")

try:
    # Cargar la imagen desde la ruta especificada
    imagen_original = cargar_imagen(ruta_imagen)

    # Solicitar al usuario que ingrese el umbral de binarización
    umbral_binarizacion = int(input("Ingrese el umbral de binarización (0-255): "))

    # Binarizar la imagen
    binarizar(imagen_original, umbral_binarizacion)

    # Guardar y mostrar la imagen binarizada
    imagen_binarizada = Image.new('RGB', (len(imagen_original[0]), len(imagen_original)))
    for y, fila in enumerate(imagen_original):
        for x, pixel in enumerate(fila):
            imagen_binarizada.putpixel((x, y), pixel)
    imagen_binarizada.show()

except FileNotFoundError:
    print("¡Error! No se encontró el archivo especificado.")
except ValueError:
    print("¡Error! El umbral de binarización debe ser un número entero.")
