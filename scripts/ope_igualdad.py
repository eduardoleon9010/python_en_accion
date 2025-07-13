# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:53:56 2024

@author: USUARIO
"""

def es_par(x: int) -> bool:
    """
    Verifica si un número entero es par.
    
    Parámetros:
    x (int): Número entero a evaluar.
    
    Retorno:
    (bool): True si el número es par, False de lo contrario.
    """
    residuo_cero = (x % 2 == 0)
    return residuo_cero

def no_es_7_v1(x: int) -> bool:
    """
    Verifica si un número entero no es igual a 7 (versión 1).
    
    Parámetros:
    x (int): Número entero a evaluar.
    
    Retorno:
    (bool): True si el número no es igual a 7, False de lo contrario.
    """
    x_es_7 = (x == 7)
    return not x_es_7

def no_es_7_v2(x: int) -> bool:
    """
    Verifica si un número entero no es igual a 7 (versión 2).
    
    Parámetros:
    x (int): Número entero a evaluar.
    
    Retorno:
    (bool): True si el número no es igual a 7, False de lo contrario.
    """
    return x != 7

# Solicitar entrada de usuario para un número entero
numero_usuario = int(input("Ingrese un número entero: "))

# Llamar a la función es_par y mostrar el resultado
resultado_par = es_par(numero_usuario)
print(f"¿El número {numero_usuario} es par? {resultado_par}")

# Llamar a la función no_es_7_v1 y mostrar el resultado
resultado_no_7_v1 = no_es_7_v1(numero_usuario)
print(f"¿El número {numero_usuario} no es igual a 7 (versión 1)? {resultado_no_7_v1}")

# Llamar a la función no_es_7_v2 y mostrar el resultado
resultado_no_7_v2 = no_es_7_v2(numero_usuario)
print(f"¿El número {numero_usuario} no es igual a 7 (versión 2)? {resultado_no_7_v2}")
