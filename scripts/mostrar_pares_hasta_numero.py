# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:28:31 2024

@author: USUARIO
"""

# Programa para mostrar números pares positivos entre 2 y un número ingresado por el usuario

def mostrar_pares_hasta_numero():
    try:
        # Solicitamos al usuario que ingrese un número
        numero_limite = int(input("Ingrese un número: "))
        
        # Verificamos que el número ingresado sea al menos 2
        if numero_limite < 2:
            print("Por favor, ingrese un número mayor o igual a 2.")
            return
        
        # Utilizamos un bucle for para iterar desde 2 hasta el número ingresado, con un paso de 2
        for numero in range(2, numero_limite + 1, 2):
            print(numero)
    
    except ValueError:
        print("Error: Ingrese un número válido.")

# Llamamos a la función para mostrar los números pares hasta el número ingresado por el usuario
mostrar_pares_hasta_numero()
1