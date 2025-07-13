# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:41:55 2024

@author: USUARIO
"""

def encontrar_mayor(entrada):
    """
    Encuentra el mayor número en una lista de enteros positivos.

    Parámetros:
    - entrada (list): Lista en la que se buscará el número mayor.

    Retorna:
    - int: El número mayor en la lista. Retorna -1 si la lista está vacía.
    """
    if not entrada:
        # Si la lista está vacía, retornamos -1.
        return -1
    else:
        # Utilizamos la función max() para encontrar el máximo en la lista.
        return max(entrada)

# Ejemplo de uso:
lista_ejemplo = [10, 5, 20, 15, 25]

# Llamamos a la función e imprimimos el resultado.
resultado = encontrar_mayor(lista_ejemplo)
print(f"El número mayor en la lista es: {resultado}")
