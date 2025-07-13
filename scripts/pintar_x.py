# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:01:44 2024

@author: USUARIO
"""
def pintar_x(matriz, operacion):
    """
    Modifica la matriz aplicando la operación indicada sobre las casillas de las diagonales.

    Args:
    - matriz (list): Matriz cuadrada con números positivos.
    - operacion (str): Cadena con el símbolo de la operación a realizar ('+', '-', '*' o '/').

    Returns:
    - list: La matriz modificada según la operación indicada.
    """
    n = len(matriz)
    
    # Verificar que la matriz sea cuadrada
    if n != len(matriz[0]):
        raise ValueError("La matriz no es cuadrada")
    
    # Iterar sobre la matriz y aplicar la operación a las diagonales
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                if operacion == '+':
                    matriz[i][j] += matriz[i][j]
                elif operacion == '-':
                    matriz[i][j] -= matriz[i][j]
                elif operacion == '*':
                    matriz[i][j] *= matriz[i][j]
                elif operacion == '/':
                    if matriz[i][j] != 0:
                        matriz[i][j] /= matriz[i][j]
                    else:
                        matriz[i][j] = 0  # Evitar división por cero
    
    return matriz

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
operacion = '*'  # Multiplicar los valores de las diagonales

print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_modificada = pintar_x(matriz, operacion)

print("\nMatriz modificada:")
for fila in matriz_modificada:
    print(fila)
