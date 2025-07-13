# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:30:49 2024

@author: USUARIO
"""

from PIL import Image

def copiar_imagen(imagen: list) -> list:
    """ 
    Crea una copia de una imagen y la retorna.

    Args:
        imagen (list): Una lista de listas de tuplas que representa una imagen.

    Returns:
        list: Una copia de la imagen.
    """
    copia = []
    alto = len(imagen)
    for i in range(0, alto):
        fila = imagen[i]
        nueva_fila = fila.copy()
        copia.append(nueva_fila)
    return copia

def sharpening(imagen: list) -> list:
    """ 
    Aplica un filtro de afilado (sharpening) sobre la imagen.

    Args:
        imagen (list): La imagen sobre la que se aplicará el filtro.

    Returns:
        list: La imagen con el resultado de aplicar el filtro de afilado.
    """
    # Se define la máscara de afilado
    mascara = [[-1, -1, -1],
               [-1, 9, -1],
               [-1, -1, -1]]

    # Se crea una copia de la imagen original
    copia = copiar_imagen(imagen)
    alto = len(imagen)
    ancho = len(imagen[0])
  
    # Se itera sobre los píxeles de la imagen
    for i in range(1, alto-1):
        for j in range(1, ancho-1):
            rojo, verde, azul = (0, 0, 0)

            # Se aplica la máscara de afilado al píxel actual y sus vecinos
            for i_mascara in range(-1, 2):
                for j_mascara in range(-1, 2):
                    rojo_vecino, verde_vecino, azul_vecino = imagen[i+i_mascara][j+j_mascara]
                    valor_mascara = mascara[i_mascara+1][j_mascara+1]

                    rojo += rojo_vecino * valor_mascara
                    verde += verde_vecino * valor_mascara
                    azul += azul_vecino * valor_mascara

            nuevo_pixel = (max(rojo, 0), max(verde, 0), max(azul, 0))
            copia[i][j] = nuevo_pixel

    return copia

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

# Solicitar al usuario que ingrese la ruta de la imagen
ruta_imagen = input("Ingrese la ruta de la imagen: ")

try:
    # Cargar la imagen desde la ruta especificada
    imagen_original = cargar_imagen(ruta_imagen)

    # Aplicar el filtro de afilado a la imagen
    imagen_filtrada = sharpening(imagen_original)

    # Crear y mostrar la imagen filtrada
    imagen_filtrada_pil = Image.new('RGB', (len(imagen_filtrada[0]), len(imagen_filtrada)))
    for y, fila in enumerate(imagen_filtrada):
        for x, pixel in enumerate(fila):
            imagen_filtrada_pil.putpixel((x, y), pixel)
    imagen_filtrada_pil.show()

except FileNotFoundError:
    print("¡Error! No se encontró el archivo especificado.")
except Exception as e:
    print("¡Error!", e)
