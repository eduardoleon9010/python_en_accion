# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:00:15 2024

@author: USUARIO
"""

def estadisticas(valores: list) -> tuple:
    """
    Calcula estadísticas básicas sobre una lista de valores.

    Args:
    valores (list): Lista de valores sobre los cuales se calcularán las estadísticas.

    Returns:
    tuple: Una tupla que contiene el valor mínimo, el valor máximo y el promedio de los valores.
    """
    # Inicializar variables para el valor mínimo, el valor máximo y el total de la suma
    menor = mayor = total = valores[0]

    # Calcular el total de la suma, el valor mínimo y el valor máximo
    for valor in valores[1:]:
        total += valor
        if valor > mayor:
            mayor = valor
        elif valor < menor:
            menor = valor
    
    # Calcular el promedio
    promedio = total / len(valores)

    return (menor, mayor, promedio)

# Ejemplo de uso
valores_ejemplo = [4, 7, 2, 10, 5]
resultado = estadisticas(valores_ejemplo)
print("Estadísticas:")
print("Valor mínimo:", resultado[0])
print("Valor máximo:", resultado[1])
print("Promedio:", resultado[2])
