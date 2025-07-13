# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:39:11 2024

@author: USUARIO
"""

def suma_matriz(matriz):
    """
    Calcula la suma de todos los valores de una matriz.

    Args:
    - matriz (list): La matriz de la cual se desea calcular la suma de los valores.

    Returns:
    - int: La suma de todos los valores de la matriz.

    Raises:
    - ValueError: Si la matriz está vacía.
    """
    if not matriz:
        raise ValueError("La matriz está vacía")
    suma = 0
    for fila in matriz:
        suma += sum(fila)
    return suma

def calcular_suma_fila(matriz, fila):
    """
    Calcula la suma de los elementos de una fila específica en una matriz.

    Args:
    - matriz (list): La matriz de la cual se desea calcular la suma de la fila.
    - fila (int): El índice de la fila para la cual se calculará la suma.

    Returns:
    - int: La suma de los elementos de la fila especificada.

    Raises:
    - ValueError: Si la fila especificada está fuera de rango.
    """
    if fila < 0 or fila >= len(matriz):
        raise ValueError("La fila está fuera de rango")
    return sum(matriz[fila])


def suma_columna(matriz, columna):
    """
    Calcula la suma de los elementos de una columna específica en una matriz.

    Args:
    - matriz (list): La matriz de la cual se desea calcular la suma de la columna.
    - columna (int): El índice de la columna para la cual se calculará la suma.

    Returns:
    - int: La suma de los elementos de la columna especificada.

    Raises:
    - ValueError: Si la columna especificada está fuera de rango.
    """
    if columna < 0 or columna >= len(matriz[0]):
        raise ValueError("La columna está fuera de rango")
    suma = 0
    for fila in matriz:
        suma += fila[columna]
    return suma


def existe_negativo(matriz):
    """
    Verifica si existe al menos un valor negativo en la matriz.

    Args:
    - matriz (list): La matriz de la cual se desea verificar la existencia de valores negativos.

    Returns:
    - bool: True si existe al menos un valor negativo, False de lo contrario.
    """
    for fila in matriz:
        for valor in fila:
            if valor < 0:
                return True
    return False

def fila_con_mas_ceros(matriz):
    """
    Encuentra la fila con la mayor cantidad de ceros en una matriz.

    Args:
    - matriz (list): La matriz en la que se desea encontrar la fila con más ceros.

    Returns:
    - int or None: El índice de la fila con más ceros, o None si la matriz está vacía.

    Example:
    matriz = [
        [1, 0, 1],
        [0, 1, 0],
        [0, 0, 0]
    ]
    fila_con_mas_ceros(matriz) -> 2
    """
    max_ceros = 0
    fila_max_ceros = None
    for i in range(len(matriz)):
        cant_ceros = sum(1 for valor in matriz[i] if valor == 0)
        if cant_ceros > max_ceros:
            max_ceros = cant_ceros
            fila_max_ceros = i
    return fila_max_ceros


# Definición de la matriz de ejemplo
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Ejemplo de uso de la función suma_matriz
suma_total = suma_matriz(matriz_ejemplo)
print("Suma total de la matriz:", suma_total)

# Ejemplo de uso de la función calcular_suma_fila
fila_deseada = 1
suma_fila_deseada = calcular_suma_fila(matriz_ejemplo, fila_deseada)
print("Suma de la fila", fila_deseada, ":", suma_fila_deseada)

# Ejemplo de uso de la función suma_columna
columna_deseada = 2
suma_columna_deseada = suma_columna(matriz_ejemplo, columna_deseada)
print("Suma de la columna", columna_deseada, ":", suma_columna_deseada)

# Ejemplo de uso de la función existe_negativo
hay_negativo = existe_negativo(matriz_ejemplo)
print("¿Hay algún valor negativo en la matriz?", hay_negativo)

# Ejemplo de uso de la función fila_con_mas_ceros
fila_max_ceros = fila_con_mas_ceros(matriz_ejemplo)
print("Fila con más ceros:", fila_max_ceros)
