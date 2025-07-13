# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 08:04:43 2024

@author: USUARIO
"""

def calcular_definitivas(estudiantes: list) -> list:
    """Calcula las notas finales aproximadas para una lista de estudiantes.

    Esta función recibe una lista de diccionarios, donde cada diccionario representa
    a un estudiante con su nombre y su nota final sin aproximar. Luego, calcula
    y retorna una lista con los mismos diccionarios actualizados con las notas
    aproximadas, según las reglas establecidas por la Universidad de los Andes.

    Args:
        estudiantes (list): Una lista de diccionarios que representan a los estudiantes
        con su nota final sin aproximar. Cada diccionario tiene las siguientes llaves:
        "nombre": (str) el nombre del estudiante.
        "nota": (float) un float que representa la nota sin aproximar del estudiante.

    Returns:
        list: Una lista de diccionarios con las notas finales aproximadas para cada estudiante.
        El orden de los diccionarios es el mismo que en la lista de entrada.
        Cada diccionario retornado tiene las llaves "nombre" (str) y "nota" (float).
    """
    notas_aproximadas = []
    for estudiante in estudiantes:
        nombre = estudiante["nombre"]
        nota = estudiante["nota"]
        if nota >= 4.5:
            nota_aproximada = 5.0
        elif nota >= 3.5:
            nota_aproximada = 4.0
        elif nota >= 2.5:
            nota_aproximada = 3.0
        else:
            nota_aproximada = 1.5
        notas_aproximadas.append({"nombre": nombre, "nota": nota_aproximada})
    return notas_aproximadas

# Ejemplo de uso:
estudiantes = [
    {"nombre": "Juan", "nota": 3.8},
    {"nombre": "María", "nota": 2.2},
    {"nombre": "Pedro", "nota": 4.7}
]
notas_finales_aproximadas = calcular_definitivas(estudiantes)
print(notas_finales_aproximadas)
