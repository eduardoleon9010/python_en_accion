# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:06:07 2024

@author: USUARIO
"""

# Programa que muestra números hasta que se ingresa un número negativo.

# Bucle while que se ejecuta hasta que se introduce un número negativo.
while True:
    # Solicitamos al usuario ingresar un número.
    numero = float(input("Ingrese un número (ingrese un número negativo para salir): "))

    # Verificamos si el número ingresado es negativo.
    if numero < 0:
        print("Hasta luego. Programa finalizado.")
        break  # Salimos del bucle al detectar un número negativo.
    else:
        # Si el número no es negativo, lo mostramos en pantalla.
        print("Número ingresado:", numero)
