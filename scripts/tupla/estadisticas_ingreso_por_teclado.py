# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 09:26:13 2024

@author: USUARIO
"""

def estadisticas_ingreso_por_teclado() -> tuple:
    """
    Calcula estadísticas básicas (mínimo, máximo y promedio) para una lista de valores
    ingresados por el usuario desde el teclado.

    Returns:
        tuple: Una tupla que contiene el valor mínimo, el valor máximo y el promedio de los valores ingresados.

    Raises:
        ValueError: Si no se ingresan valores válidos.

    Example:
        >>> estadisticas_ingreso_por_teclado()
        Por favor, ingrese una lista de valores separados por espacios: 1 2 3 4 5
        Estadísticas para los valores ingresados:
        - Valor mínimo: 1
        - Valor máximo: 5
        - Promedio: 3.00
        (1, 5, 3.0)
    """
    # Ingresar los valores desde el teclado
    valores_str = input("Por favor, ingrese una lista de valores separados por espacios: ")
    valores_str = valores_str.strip()
    
    # Verificar si se ingresaron valores
    if not valores_str:
        raise ValueError("No se ingresaron valores válidos.")

    # Convertir los valores a una lista de números
    valores = [float(valor) for valor in valores_str.split()]

    # Verificar si la lista de valores no está vacía
    if not valores:
        raise ValueError("No se ingresaron valores válidos.")

    # Inicializar variables para el mayor, el menor y el total
    mayor = menor = valores[0]
    total = sum(valores)

    # Calcular el mayor y el menor
    for valor in valores:
        if valor > mayor:
            mayor = valor
        elif valor < menor:
            menor = valor

    # Calcular el promedio con solo dos decimales
    promedio = total / len(valores)

    # Imprimir las estadísticas
    print("Estadísticas para los valores ingresados:")
    print("- Valor mínimo:", menor)
    print("- Valor máximo:", mayor)
    print("- Promedio: {:.2f}".format(promedio))

    return (menor, mayor, promedio)


# Ejemplo de uso de la función estadisticas_ingreso_por_teclado
resultado = estadisticas_ingreso_por_teclado()
print("Resultado:", resultado)
