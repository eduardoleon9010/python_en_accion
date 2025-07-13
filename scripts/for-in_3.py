# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:49:17 2024

@author: USUARIO
"""

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese el número del cual necesitas ver la tabla de multiplicar: "))

# Mostrar la tabla de multiplicar del número ingresado
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 13):  # Iterar desde 1 hasta 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
