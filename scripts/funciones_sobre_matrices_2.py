# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:45:21 2024

@author: USUARIO
"""

def crear_matriz(filas, columnas):
    """
    Crea una matriz de tamaño dado por el usuario.

    Args:
    - filas (int): El número de filas de la matriz.
    - columnas (int): El número de columnas de la matriz.

    Returns:
    - list: La matriz creada por el usuario.
    """
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el valor para la fila {i+1}, columna {j+1}: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

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

# Solicitar al usuario el tamaño de la matriz
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

# Crear la matriz
matriz = crear_matriz(filas, columnas)

# Calcular y mostrar resultados
print("Suma de la matriz:", suma_matriz(matriz))

fila = int(input("Ingrese el número de la fila para calcular su suma: "))
print("Suma de la fila:", calcular_suma_fila(matriz, fila))

columna = int(input("Ingrese el número de la columna para calcular su suma: "))
print("Suma de la columna:", suma_columna(matriz, columna))

if existe_negativo(matriz):
    print("La matriz contiene al menos un valor negativo.")
else:
    print("La matriz no contiene valores negativos.")

fila_max_ceros = fila_con_mas_ceros(matriz)
if fila_max_ceros is not None:
    print("La fila con más ceros es la fila:", fila_max_ceros)
else:
    print("La matriz está vacía o no contiene ceros.")

