# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 15:38:55 2024

@author: USUARIO
"""

def comprimir(cadena: str) -> tuple:
    """
    Recibe una cadena de ceros y unos y devuelve una tupla con dos elementos: la longitud original de la cadena
    y una lista de tuplas que contienen la posición y la cantidad de unos seguidos en la cadena original.

    Args:
        cadena (str): La cadena de ceros y unos a comprimir.

    Returns:
        tuple: Una tupla que contiene la longitud original de la cadena y una lista de tuplas con las posiciones y
        las cantidades de unos seguidos.

    Example:
        >>> comprimir('101101111000110')
        (15, [(0, 1), (2, 2), (5, 4), (12, 2)])
    """
    longitud_original = len(cadena)
    secuencias_unos = []
    contador = 0

    # Iterar sobre la cadena
    for i, bit in enumerate(cadena):
        if bit == '1':
            contador += 1
        elif contador > 0:
            secuencias_unos.append((i - contador, contador))
            contador = 0

    # Manejar el último grupo de unos si es necesario
    if contador > 0:
        secuencias_unos.append((len(cadena) - contador, contador))

    return longitud_original, secuencias_unos


# Ejemplo de uso de la función comprimir
cadena_ejemplo = '101101111000110'
resultado_comprimir = comprimir(cadena_ejemplo)
print("Resultado de comprimir la cadena:", resultado_comprimir)
