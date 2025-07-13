# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:26:58 2024

@author: USUARIO
"""

import math

def ingresar_vector():
    x = float(input("Ingrese la coordenada x: "))
    y = float(input("Ingrese la coordenada y: "))
    z = float(input("Ingrese la coordenada z: "))
    return [x, y, z]

def calcular_suma(vector1, vector2):
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]

def calcular_diferencia(vector1, vector2):
    return [v1 - v2 for v1, v2 in zip(vector1, vector2)]

def calcular_producto_escalar(vector1, vector2):
    return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

def calcular_producto_vectorial(vector1, vector2):
    if len(vector1) == 3 and len(vector2) == 3:
        x = vector1[1] * vector2[2] - vector1[2] * vector2[1]
        y = vector1[2] * vector2[0] - vector1[0] * vector2[2]
        z = vector1[0] * vector2[1] - vector1[1] * vector2[0]
        return [x, y, z]
    else:
        print("Error: Los vectores deben tener tres componentes (x, y, z).")
        print(f"Vector 1: {vector1}")
        print(f"Vector 2: {vector2}")
        return None



def calcular_angulo_entre_vectores(vector1, vector2):
    try:
        producto_escalar = calcular_producto_escalar(vector1, vector2)
        magnitud_vector1 = math.sqrt(sum(v ** 2 for v in vector1))
        magnitud_vector2 = math.sqrt(sum(v ** 2 for v in vector2))
        coseno_angulo = producto_escalar / (magnitud_vector1 * magnitud_vector2)
        angulo_radianes = math.acos(coseno_angulo)
        angulo_grados = math.degrees(angulo_radianes)
        return angulo_grados
    except ZeroDivisionError:
        print("Error: División por cero al calcular el ángulo.")
        return None

def calcular_longitud(vector):
    try:
        return math.sqrt(sum(v ** 2 for v in vector))
    except ValueError:
        print("Error: Raíz cuadrada de un argumento negativo al calcular la longitud.")
        return None

def sub_menu_orden():
    print("\nSeleccione el orden de los operandos:")
    print("1) Vector1 - Vector2")
    print("2) Vector2 - Vector1")
    opcion = int(input("Ingrese el número de la opción: "))
    return opcion

def menu_principal():
    vector1 = []
    vector2 = []

    while True:
        print("\nSeleccione una opción:")
        print("1) Introducir el primer vector")
        print("2) Introducir el segundo vector")
        print("3) Calcular la suma")
        print("4) Calcular la diferencia")
        print("5) Calcular el producto escalar")
        print("6) Calcular el producto vectorial")
        print("7) Calcular el ángulo entre ellos (en grados)")
        print("8) Calcular la longitud")
        print("9) Finalizar")
        opcion = int(input("Ingrese el número de la opción: "))

        if opcion == 1:
            vector1 = ingresar_vector()
        elif opcion == 2:
            vector2 = ingresar_vector()
        elif opcion == 3:
            resultado = calcular_suma(vector1, vector2)
            print(f"La suma de los vectores es: {resultado}")
        elif opcion == 4:
            sub_opcion = sub_menu_orden()
            if sub_opcion == 1:
                resultado = calcular_diferencia(vector1, vector2)
            elif sub_opcion == 2:
                resultado = calcular_diferencia(vector2, vector1)
            print(f"La diferencia de los vectores es: {resultado}")
        elif opcion == 5:
            resultado = calcular_producto_escalar(vector1, vector2)
            print(f"El producto escalar de los vectores es: {resultado}")
        elif opcion == 6:
            resultado = calcular_producto_vectorial(vector1, vector2)
            print(f"El producto vectorial de los vectores es: {resultado}")
        elif opcion == 7:
            resultado = calcular_angulo_entre_vectores(vector1, vector2)
            if resultado is not None:
                print(f"El ángulo entre los vectores es: {resultado} grados")
        elif opcion == 8:
            sub_opcion = sub_menu_orden()
            if sub_opcion == 1:
                resultado = calcular_longitud(vector1)
            elif sub_opcion == 2:
                resultado = calcular_longitud(vector2)
            if resultado is not None:
                print(f"La longitud del vector es: {resultado}")
        elif opcion == 9:
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu_principal()
