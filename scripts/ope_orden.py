# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:50:09 2024

@author: USUARIO
"""

def es_positivo(x: int) -> bool:
    """
    Verifica si un número entero es positivo.
    
    Parámetros:
    x (int): Número entero a evaluar.
    
    Retorno:
    (bool): True si el número es positivo, False de lo contrario.
    """
    positivo = x > 0
    return positivo

def es_negativo(x: int) -> bool:
    """
    Verifica si un número entero es negativo.
    
    Parámetros:
    x (int): Número entero a evaluar.
    
    Retorno:
    (bool): True si el número es negativo, False de lo contrario.
    """
    negativo = x < 0
    return negativo

def es_cero(x: int) -> bool:
    """
    Verifica si un número entero es igual a cero.
    
    Parámetros:
    x (int): Número entero a evaluar.
    
    Retorno:
    (bool): True si el número es cero, False de lo contrario.
    """
    positivo = es_positivo(x)
    negativo = es_negativo(x)
    return not positivo and not negativo

def ordenadas(antes: str, despues: str) -> bool:
    """
    Verifica si dos cadenas están ordenadas lexicográficamente en un diccionario.
    
    Parámetros:
    antes (str): Una cadena que está antes que la otra en un diccionario.
    despues (str): Una cadena que está después que la otra en un diccionario.
    
    Retorno:
    (bool): True si las cadenas están ordenadas lexicográficamente,
            False de lo contrario.
    """
    estan_ordenadas = antes < despues
    return estan_ordenadas

# Solicitar entrada de usuario para un número entero
numero_entero = int(input("Ingrese un número entero: "))

# Llamar a la función es_positivo y mostrar el resultado
resultado_positivo = es_positivo(numero_entero)
print(f"¿El número {numero_entero} es positivo? {resultado_positivo}")

# Llamar a la función es_negativo y mostrar el resultado
resultado_negativo = es_negativo(numero_entero)
print(f"¿El número {numero_entero} es negativo? {resultado_negativo}")

# Llamar a la función es_cero y mostrar el resultado
resultado_cero = es_cero(numero_entero)
print(f"¿El número {numero_entero} es cero? {resultado_cero}")

# Solicitar entrada de usuario para dos cadenas
cadena_antes = input("Ingrese una cadena que esté antes en un diccionario: ")
cadena_despues = input("Ingrese una cadena que esté después en un diccionario: ")

# Llamar a la función ordenadas y mostrar el resultado
resultado_ordenadas = ordenadas(cadena_antes, cadena_despues)
print(f"¿Las cadenas están ordenadas lexicográficamente? {resultado_ordenadas}")
