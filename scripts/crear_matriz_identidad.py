# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:31:52 2024

@author: USUARIO
"""

def crear_matriz_identidad(n):
    """
    Crea una matriz identidad de tamaño n por n.

    Args:
    n (int): El tamaño de la matriz.

    Returns:
    list: Una lista de listas que representa la matriz identidad.
    """
    # Inicializar la matriz con ceros
    matriz_identidad = [[0] * n for _ in range(n)]

    # Colocar unos en la diagonal principal
    for i in range(n):
        matriz_identidad[i][i] = 1

    return matriz_identidad

def imprimir_matriz(matriz):
    """
    Imprime una matriz en formato de tabla.

    Args:
    matriz (list): Una lista de listas que representa la matriz.
    """
    for fila in matriz:
        print(" ".join(map(str, fila)))

if __name__ == "__main__":
    # Solicitar al usuario el tamaño de la matriz identidad
    n = int(input("Ingrese el tamaño de la matriz identidad: "))

    # Crear la matriz identidad
    matriz_identidad = crear_matriz_identidad(n)

    # Imprimir la matriz identidad
    print("Matriz Identidad:")
    imprimir_matriz(matriz_identidad)
