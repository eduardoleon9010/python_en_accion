# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 08:07:45 2024

@author: USUARIO
"""

def calcular_definitivas():
    estudiantes = []
    num_estudiantes = int(input("Ingrese el número de estudiantes: "))
    for i in range(num_estudiantes):
        nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
        nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
        estudiantes.append({"nombre": nombre, "nota": nota})

    def aproximar_nota(nota):
        if nota >= 4.5:
            return 5.0
        elif nota >= 3.5:
            return 4.0
        elif nota >= 2.5:
            return 3.0
        else:
            return 1.5

    estudiantes_actualizados = []
    for estudiante in estudiantes:
        estudiantes_actualizados.append({"nombre": estudiante["nombre"], "nota": aproximar_nota(estudiante["nota"])})

    return estudiantes_actualizados

# Ejemplo de uso
if __name__ == "__main__":
    estudiantes_aproximados = calcular_definitivas()
    print("Notas aproximadas de los estudiantes:")
    for estudiante in estudiantes_aproximados:
        print(f"Nombre: {estudiante['nombre']}, Nota: {estudiante['nota']}")
