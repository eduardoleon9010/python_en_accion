# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:08:00 2024

@author: USUARIO
"""

# Programa que muestra el número mayor entre los ingresados hasta que se ingresa un número negativo.

# Inicializamos la variable para almacenar el número mayor.
numero_mayor = float('-inf')

# Bucle while que se ejecuta hasta que se introduce un número negativo.
while True:
    # Solicitamos al usuario ingresar un número.
    numero = float(input("Ingrese un número (ingrese un número negativo para salir): "))

    # Verificamos si el número ingresado es negativo.
    if numero < 0:
        if numero_mayor == float('-inf'):
            print("No se ha ingresado ningún número antes de salir.")
        else:
            # Mostramos el número mayor.
            print("El número mayor ingresado es:", numero_mayor)
        print("Hasta luego. Programa finalizado.")
        break  # Salimos del bucle al detectar un número negativo.
    else:
        # Comparamos con el número mayor actual y actualizamos si es necesario.
        if numero > numero_mayor:
            numero_mayor = numero
