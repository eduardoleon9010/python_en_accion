# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:48:37 2024

@author: USUARIO
"""
def promedio_fila():
    """
    Calcula el promedio de la nota de una fila en una matriz.

    Returns:
    - float: El promedio de la fila redondeado a dos decimales.
    """
    # Pedir al usuario la matriz como una lista de listas
    matriz = []
    while True:
        fila = input("Ingrese la fila del salón como una lista separada por comas (0 para representar que no hay estudiantes): ")
        if fila == "":
            break
        fila_lista = [int(valor) for valor in fila.split(",")]
        matriz.append(fila_lista)
    
    # Pedir al usuario el número de fila para calcular el promedio
    fila = int(input("Ingrese el número de la fila para calcular el promedio: "))
    
    # Verificar si la fila solicitada existe en la matriz
    if fila < 1 or fila > len(matriz):
        print("El número de fila especificado no es válido.")
        return -1
    
    # Obtener la fila correspondiente
    fila_matriz = matriz[fila - 1]
    
    # Verificar si la fila está vacía
    if all(valor == 0 for valor in fila_matriz):
        print("La fila está vacía.")
        return 0
    
    # Calcular el promedio de la fila
    suma_notas = sum(fila_matriz)
    cantidad_estudiantes = sum(1 for valor in fila_matriz if valor != 0)
    promedio = suma_notas / cantidad_estudiantes
    
    return round(promedio, 2)

# Llamar a la función para calcular el promedio de la fila
resultado = promedio_fila()
print("El promedio de la fila es:", resultado)
