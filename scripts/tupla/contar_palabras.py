# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 15:37:59 2024

@author: USUARIO
"""

def contar_palabras(cadena: str) -> list:
    """
    Recibe una cadena de caracteres y retorna una lista de tuplas donde la primera posición corresponde a una palabra que aparece en la cadena
    y la segunda posición corresponde a la cantidad de veces que aparece la palabra en la cadena.

    Args:
        cadena (str): La cadena de caracteres de entrada.

    Returns:
        list: Una lista de tuplas donde cada tupla contiene una palabra y la cantidad de veces que aparece en la cadena original.

    Example:
        >>> contar_palabras("Esta es una cadena de ejemplo con palabras repetidas como esta y esta")
        [('Esta', 1), ('es', 1), ('una', 1), ('cadena', 1), ('de', 1), ('ejemplo', 1), ('con', 1), ('palabras', 1), ('repetidas', 1), ('como', 1), ('esta', 2), ('y', 1)]
    """
    # Dividir la cadena en palabras
    palabras = cadena.split()

    # Crear un diccionario para contar las ocurrencias de cada palabra
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1

    # Convertir el diccionario en una lista de tuplas
    lista_parejas = [(palabra, conteo[palabra]) for palabra in conteo]

    return lista_parejas


# Ejemplo de uso de la función contar_palabras
cadena = "Esta es una cadena de ejemplo con palabras repetidas como esta y esta"
resultado = contar_palabras(cadena)
print("Resultado de contar palabras:", resultado)
