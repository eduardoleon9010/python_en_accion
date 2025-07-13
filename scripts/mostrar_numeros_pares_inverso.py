# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:25:33 2024

@author: USUARIO
"""

# Programa para mostrar números pares en orden inverso entre 0 y 200

def mostrar_numeros_pares_inverso():
    # Utilizamos el rango desde 200 hasta 0 con un paso de -2 para obtener números pares en orden inverso
    for numero in range(200, -1, -2):
        print(numero)

# Llamamos a la función para mostrar los números pares en orden inverso
mostrar_numeros_pares_inverso()
