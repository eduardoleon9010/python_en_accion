# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 15:39:33 2024

@author: USUARIO
"""

def descomprimir(resultado_comprimir: tuple) -> str:
    """
    Recibe el resultado de la función comprimir y produce la cadena original.

    Args:
        resultado_comprimir (tuple): Una tupla que contiene la longitud original de la cadena y una lista de tuplas
        con las posiciones y las cantidades de unos seguidos.

    Returns:
        str: La cadena original antes de la compresión.

    Example:
        >>> descomprimir((15, [(0, 1), (2, 2), (5, 4), (12, 2)]))
        '101101111000110'
    """
    longitud_original, secuencias_unos = resultado_comprimir
    cadena_original = ''

    for posicion, cantidad in secuencias_unos:
        cadena_original += '1' * cantidad
        cadena_original += '0' * (posicion - len(cadena_original) + 1)

    cadena_original += '0' * (longitud_original - len(cadena_original))
    
    return cadena_original


# Ejemplo de uso de la función descomprimir
resultado_comprimir_ejemplo = (15, [(0, 1), (2, 2), (5, 4), (12, 2)])
cadena_original = descomprimir(resultado_comprimir_ejemplo)
print("Cadena original después de descomprimir:", cadena_original)
