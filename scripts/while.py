# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 08:48:01 2024

@author: USUARIO
"""

# Diseño de un programa que solicita la lectura de un número entre 0 y 10.

# Inicializamos la variable numero con un valor fuera del rango para que entre al bucle.
numero = -1

# Bucle while que se ejecuta mientras el número ingresado esté fuera del rango [0, 10].
while numero < 0 or numero > 10:
    try:
        # Solicitamos al usuario ingresar un número
        numero = int(input("Ingrese un número entre 0 y 10 (inclusive): "))
        
        # Verificamos si el número está fuera del rango
        if numero < 0 or numero > 10:
            print("Número fuera del rango. Inténtelo nuevamente.")
    except ValueError:
        # Manejo de excepción para el caso en que el usuario ingrese algo que no sea un número.
        print("Error: Ingrese un valor numérico válido.")

# Fuera del bucle, se imprime el número válido ingresado.
print("Número válido ingresado:", numero)
