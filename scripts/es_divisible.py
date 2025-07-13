# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 02:17:19 2024

@author: USUARIO
"""

def es_divisible(num1: int, num2: int) -> bool:
    """
    Verifica si el primer número es divisible por el segundo.
    
    Parámetros:
    num1 (int): Primer número.
    num2 (int): Segundo número.
    
    Retorno:
    (bool): True si el primer número es divisible por el segundo, False de lo contrario.
    """
    # Verificar si el segundo número es diferente de cero para evitar divisiones por cero
    if num2 != 0:
        return num1 % num2 == 0
    else:
        print("Error: El segundo número no puede ser cero.")
        return False

# Ejemplo de uso de la función
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if es_divisible(numero1, numero2):
    print(f"{numero1} es divisible por {numero2}.")
else:
    print(f"{numero1} no es divisible por {numero2}.")
