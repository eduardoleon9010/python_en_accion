# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 08:44:28 2024

@author: USUARIO
"""

# Inicializamos la variable suma en 0
suma = 0

# Solicitamos al usuario ingresar un número
numero = int(input("Ingrese un número (o 0 para finalizar): "))

# Bucle while que se ejecuta mientras el número ingresado sea diferente de 0
while numero != 0:
    # Sumamos el número al acumulador 'suma'
    suma += numero
    
    # Solicitamos al usuario ingresar otro número o 0 para finalizar
    numero = int(input("Ingrese otro número (o 0 para finalizar): "))

# Fuera del bucle, imprimimos la suma total de los números ingresados
print("La suma total es:", suma)
