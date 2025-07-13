# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:04:47 2024

@author: USUARIO
"""

def construir_diccionario_alturas():
    """
    Construye un diccionario con las alturas sobre el nivel del mar de las capitales de los países suramericanos.

    Retorno:
    - dict: Un diccionario donde las llaves son los nombres de las ciudades y los valores son las alturas.
    """
    alturas_capitales = {
        'Bogotá': 2640,
        'Buenos Aires': 25,
        'Lima': 154,
        'Asunción': 43,
        'Quito': 2850,
        'Montevideo': 43,
        'Caracas': 920,
        'Brasilia': 1172,
        'Santiago': 520,
        'Lisboa': 220  # Este ejemplo es solo adicional, ya que Lisboa no es una capital suramericana.
    }
    return alturas_capitales

def ciudad_mayor_altura(diccionario_alturas: dict, ciudad1: str, ciudad2: str) -> str:
    """
    Compara las alturas de dos ciudades y retorna el nombre de la ciudad ubicada a mayor altura.

    Parámetros:
    - diccionario_alturas (dict): Un diccionario donde las llaves son los nombres de las ciudades y los valores son las alturas.
    - ciudad1 (str): El nombre de la primera ciudad a comparar.
    - ciudad2 (str): El nombre de la segunda ciudad a comparar.

    Retorno:
    - str: El nombre de la ciudad ubicada a mayor altura. Si alguno de los nombres no corresponde a una ciudad, retorna None.
    """
    ciudad1_lower = ciudad1.lower()
    ciudad2_lower = ciudad2.lower()

    altura_ciudad1 = diccionario_alturas.get(ciudad1_lower, None)
    altura_ciudad2 = diccionario_alturas.get(ciudad2_lower, None)

    if altura_ciudad1 is None or altura_ciudad2 is None:
        return None

    if altura_ciudad1 > altura_ciudad2:
        return ciudad1
    elif altura_ciudad1 < altura_ciudad2:
        return ciudad2
    else:
        return "Empate"

# Ejemplo de uso
diccionario_alturas = construir_diccionario_alturas()
nombre_ciudad_mayor_altura = ciudad_mayor_altura(diccionario_alturas, 'Bogotá', 'Buenos Aires')

# Imprimir el resultado
print(f"La ciudad ubicada a mayor altura es: {nombre_ciudad_mayor_altura}")
