# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 08:39:44 2024

@author: USUARIO
"""

def f(x: int) -> bool:
    """
    Esta función imprime el valor de 'x' precedido por 'f:', 
    y luego devuelve True.
    
    Parámetros:
    - x (int): El valor de entrada entero.

    Retorna:
    - bool: Siempre retorna True.
    """
    print('f:', x)
    return True

def g(x: int) -> bool:
    """
    Esta función imprime el valor de 'x' precedido por 'g:', 
    y luego devuelve False.
    
    Parámetros:
    - x (int): El valor de entrada entero.

    Retorna:
    - bool: Siempre retorna False.
    """
    print('g:', x)
    return False

# Caso 1 - f or f or f
print("Caso 1 - f or f or f :")
print(f(1) or f(2) or f(3))

# Caso 2 - f or f or g
print("Caso 2 - f or f or g :")
print(f(1) or f(2) or g(3))

# Caso 3 - g or f or g
print("Caso 3 - g or f or g :")
print(g(1) or f(2) or g(3))

# Caso 4 - g or g or g
print("Caso 4 - g or g or g :")
print(g(1) or g(2) or g(3))
