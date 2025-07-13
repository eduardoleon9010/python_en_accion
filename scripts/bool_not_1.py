# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 08:44:22 2024

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

# Caso 1
print("Caso 1:", not f(1) and f(2))
print(not f(1) and f(2))

# Caso 2
print("Caso 2:", not g(1) and f(2))
print(not g(1) and f(2))
