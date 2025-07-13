# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:03:07 2024

@author: USUARIO
"""

# Diseño de un programa que solicita la lectura de un texto sin letras mayúsculas.

# Bucle while que se ejecuta mientras haya al menos una letra mayúscula en el texto.
while True:
    # Solicitamos al usuario ingresar un texto.
    texto = input("Ingrese un texto sin letras mayúsculas: ")

    # Verificamos si hay alguna letra mayúscula en el texto.
    if any(letra.isupper() for letra in texto):
        print("Error: El texto no debe contener letras mayúsculas. Inténtelo nuevamente.")
    else:
        # Fuera del bucle si no hay letras mayúsculas, se imprime el texto y se sale del bucle.
        print("Texto válido ingresado:", texto)
        break
