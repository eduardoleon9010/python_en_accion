# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:14:05 2024

@author: USUARIO
"""

def calcular_estadisticas_tarea(estudiantes_tareas, nombre_tarea):
    """
    Calcula las estadísticas para una tarea dada.

    Args:
    estudiantes_tareas (dict): Un diccionario de diccionarios con la información de los estudiantes y sus tareas.
    nombre_tarea (str): El nombre de la tarea para la que se quiere calcular las estadísticas.

    Returns:
    dict: Un diccionario con las llaves "mayor", "mejor", "menor", "peor", "promedio", "cantidad" y "total" que representan:
    la mayor nota, el nombre del estudiante con la mejor nota, la peor nota, el nombre del estudiante con la peor nota, el promedio,
    la cantidad de estudiantes que hicieron la tarea y el valor total que resulta de sumar todas las notas obtenidas en esa tarea.
    """
    # Inicializar variables para las estadísticas
    mayor_nota = float('-inf')
    mejor_estudiante = ''
    menor_nota = float('inf')
    peor_estudiante = ''
    cantidad_estudiantes = 0
    total_notas = 0

    # Recorrer el diccionario de estudiantes y tareas
    for estudiante, tareas in estudiantes_tareas.items():
        if nombre_tarea in tareas:
            nota = tareas[nombre_tarea]
            # Actualizar la mayor nota y el mejor estudiante
            if nota > mayor_nota:
                mayor_nota = nota
                mejor_estudiante = estudiante
            # Actualizar la menor nota y el peor estudiante
            if nota < menor_nota:
                menor_nota = nota
                peor_estudiante = estudiante
            # Actualizar la cantidad de estudiantes y el total de notas
            cantidad_estudiantes += 1
            total_notas += nota

    # Calcular el promedio de las notas
    promedio = total_notas / cantidad_estudiantes if cantidad_estudiantes != 0 else 0

    # Crear el diccionario con las estadísticas
    estadisticas = {
        "mayor": mayor_nota,
        "mejor": mejor_estudiante,
        "menor": menor_nota,
        "peor": peor_estudiante,
        "promedio": promedio,
        "cantidad": cantidad_estudiantes,
        "total": total_notas
    }

    return estadisticas

# Ejemplo de uso
if __name__ == "__main__":
    # Diccionario de estudiantes y tareas
    estudiantes_tareas = {
        "Roberto": {"Tarea 1": 80, "Tarea 2": 90, "Tarea 3": 70},
        "María": {"Tarea 1": 85, "Tarea 2": 95},
        "Carlos": {"Tarea 2": 100, "Tarea 3": 75},
        "Ana": {"Tarea 1": 60, "Tarea 3": 85}
    }

    # Nombre de la tarea para calcular estadísticas
    tarea = "Tarea 2"

    # Calcular estadísticas para la tarea dada
    estadisticas = calcular_estadisticas_tarea(estudiantes_tareas, tarea)
    print(f"Estadísticas para la tarea '{tarea}': {estadisticas}")
