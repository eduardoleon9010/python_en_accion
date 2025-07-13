# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 21:41:01 2024

@author: USUARIO
"""

def crear_figura(posicion, tamano):
    """
    Crea un diccionario que representa un rectángulo con la posición y tamaño dados.

    Args:
        posicion (tuple): Tupla con las coordenadas (x, y) de la esquina superior izquierda del rectángulo.
        tamano (tuple): Tupla con el ancho y alto del rectángulo.

    Returns:
        dict: Diccionario representando el rectángulo con las propiedades especificadas.
    """
    # Inicializar el diccionario con las llaves pos y tamaño
    figura = {
        'pos': posicion,
        'tamaño': tamano,
        # Resto de las propiedades con valores por defecto
        'esquinas_redondeadas': False,
        'grosor_linea': 3,
        'color_relleno': None,
        'color_linea': (0, 0, 0),  # Negro
        'rotacion': (0, 0, 0)
    }

    return figura

# Ejemplo de uso
posicion = (100, 100)
tamano = (200, 150)
rectangulo = crear_figura(posicion, tamano)
print(rectangulo)
