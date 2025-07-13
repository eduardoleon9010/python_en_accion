# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:53:44 2024

@author: USUARIO
"""

def saludar(nombre: str)-> str:
 return "Hola " + nombre + "!"
nombre = input("¿Cuál es su nombre? ")
saludo = saludar(nombre)
print(saludo)
