# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:22:11 2024

@author: USUARIO
"""
import random

def lanzar_dado(resultados: dict) -> None:
    """
    Lanza un dado calculando aleatoriamente un número entre 1 y 6.
    
    Parámetros:
    - resultados (dict): Un diccionario que representa el conjunto de valores diferentes obtenidos.
    """
    valor = random.randint(1, 6)
    resultados[valor] = True

def lanzar_6_dados() -> dict:
    """
    Lanza el dado 6 veces y retorna un diccionario con los valores que se obtuvieron.
    
    Retorno:
    (dict): Un diccionario donde sólo aparecen como llaves los valores que se obtuvieron en el lanzamiento del dado.
    """
    resultados = {}
    for _ in range(6):
        lanzar_dado(resultados)
    return resultados

def contar_resultados_diferentes(resultados: dict) -> int:
    """
    Cuenta cuántos resultados diferentes hubo.
    
    Parámetros:
    - resultados (dict): El conjunto de los resultados obtenidos representado utilizando un diccionario.
    
    Retorno:
    (int): La cantidad de resultados diferentes que hubo.
    """
    return len(resultados)

# Lanzar el dado 6 veces y registrar los resultados obtenidos
resultados = lanzar_6_dados()

# Contar cuántos valores diferentes se obtuvieron
diferentes = contar_resultados_diferentes(resultados)
print("En 6 lanzamientos del dado se obtuvieron", diferentes, "valores diferentes")
