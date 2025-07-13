# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:09:44 2024

@author: USUARIO
"""

def letra_mas_comun(cadena: str) -> str:
    """
    Encuentra la letra más común (moda) en una cadena y la devuelve.

    Parámetros:
        cadena (str): La cadena de texto en la que se quiere encontrar la letra más común.

    Retorna:
        str: La letra más común en la cadena dada.

    Descripción del retorno:
        Retorna la letra más común en la cadena dada. En caso de que haya dos o más letras con la misma cantidad
        de apariciones, se devuelve la letra que sea alfabéticamente posterior.

    Ejemplo:
        >>> letra_mas_comun("Hoy es un buen día")
        'u'
    """
    # Eliminar espacios, puntos y comas para simplificar el análisis
    cadena = cadena.replace(' ', '').replace('.', '').replace(',', '')

    # Crear un diccionario para contar la frecuencia de cada letra
    frecuencia_letras = {}
    for letra in cadena:
        if letra in frecuencia_letras:
            frecuencia_letras[letra] += 1
        else:
            frecuencia_letras[letra] = 1

    # Encontrar la letra con la frecuencia máxima
    max_frecuencia = max(frecuencia_letras.values())
    moda = [letra for letra, frecuencia in frecuencia_letras.items() if frecuencia == max_frecuencia]

    # Ordenar alfabéticamente y devolver la última letra
    return sorted(moda)[-1]

# Ejemplo de uso
cadena = "Hoy es un buen día"
print(letra_mas_comun(cadena))  # Salida esperada: 'u'

    