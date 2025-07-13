# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 09:48:42 2024

@author: USUARIO
"""

def sumar_vectores(vector1: tuple, vector2: tuple) -> tuple:
    """
    Realiza la suma de dos vectores y devuelve el resultado como una nueva tupla que representa el vector resultante.

    Args:
        vector1 (tuple): Tupla que contiene las coordenadas (x, y) del primer vector.
        vector2 (tuple): Tupla que contiene las coordenadas (x, y) del segundo vector.

    Returns:
        tuple: Una tupla que contiene los componentes x e y del vector resultante.

    Example:
        >>> sumar_vectores((1.5, 2.5), (3.5, 4.5))
        El vector resultante de la suma es: (5.0, 7.0)
        (5.0, 7.0)
    """
    # Desempaquetar las coordenadas de los vectores
    x1, y1 = vector1
    x2, y2 = vector2

    # Calcular las componentes del vector resultante
    x_resultante = x1 + x2
    y_resultante = y1 + y2

    # Mostrar el vector resultante y retornarlo
    print("El vector resultante de la suma es:", (x_resultante, y_resultante))
    return (x_resultante, y_resultante)


# Ejemplo de uso de la función sumar_vectores con vectores proporcionados directamente
resultado_suma = sumar_vectores((1.5, 2.5), (3.5, 4.5))
print("Resultado de la suma de vectores:", resultado_suma)
