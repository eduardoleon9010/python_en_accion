# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 08:30:45 2024

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

# Caso 1 - f and f and f
print("Caso 1 - f and f and f :")
print(f(1) and f(2) and f(3))

# Caso 2 - f and f and g
print("Caso 2 - f and f and g :")
print(f(1) and f(2) and g(3))

# Caso 3 - f and g and g
print("Caso 3 - f and g and g :")
print(f(1) and g(2) and g(3))

# Caso 4 - g and g and g
print("Caso 4 - g and g and g :")
print(g(1) and g(2) and g(3))
