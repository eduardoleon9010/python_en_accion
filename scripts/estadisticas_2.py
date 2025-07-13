# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:07:02 2024

@author: USUARIO
"""

def estadisticas() -> tuple:
    """
    Calcula estadísticas básicas sobre una lista de valores ingresados por el usuario.

    Returns:
    tuple: Una tupla que contiene el valor mínimo, el valor máximo y el promedio de los valores ingresados.
    """
    valores = []

    # Solicitar al usuario que ingrese los valores
    while True:
        valor_str = input("Ingresa un valor (o 'fin' para terminar): ")
        if valor_str.lower() == 'fin':
            break
        try:
            valor = float(valor_str)
            valores.append(valor)
        except ValueError:
            print("¡Valor no válido! Por favor ingresa un número válido.")

    # Verificar si se ingresaron valores
    if not valores:
        print("No se ingresaron valores.")
        return (None, None, None)

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
print("Ingresa una serie de valores para calcular estadísticas.")
resultado = estadisticas()
print("Estadísticas:")
print("Valor mínimo:", resultado[0])
print("Valor máximo:", resultado[1])
print("Promedio:", resultado[2])
