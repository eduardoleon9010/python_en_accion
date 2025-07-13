# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:21:13 2024

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
    x = vector1[1] * vector2[2] - vector1[2] * vector2[1]
    y = vector1[2] * vector2[0] - vector1[0] * vector2[2]
    z = vector1[0] * vector2[1] - vector1[1] * vector2[0]
    return [x, y, z]

def calcular_angulo_entre_vectores(vector1, vector2):
    producto_escalar = calcular_producto_escalar(vector1, vector2)
    magnitud_vector1 = math.sqrt(sum(v ** 2 for v in vector1))
    magnitud_vector2 = math.sqrt(sum(v ** 2 for v in vector2))
    coseno_angulo = producto_escalar / (magnitud_vector1 * magnitud_vector2)
    angulo_radianes = math.acos(coseno_angulo)
    angulo_grados = math.degrees(angulo_radianes)
    return angulo_grados

def calcular_longitud(vector):
    return math.sqrt(sum(v ** 2 for v in vector))

# Vectores iniciales
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
        print("La suma de los vectores es:", calcular_suma(vector1, vector2))
    elif opcion == 4:
        print("La diferencia entre los vectores es:", calcular_diferencia(vector1, vector2))
    elif opcion == 5:
        print("El producto escalar de los vectores es:", calcular_producto_escalar(vector1, vector2))
    elif opcion == 6:
        print("El producto vectorial de los vectores es:", calcular_producto_vectorial(vector1, vector2))
    elif opcion == 7:
        print("El ángulo entre los vectores es:", calcular_angulo_entre_vectores(vector1, vector2), "grados")
    elif opcion == 8:
        print("La longitud del vector es:", calcular_longitud(vector1))
    elif opcion == 9:
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
