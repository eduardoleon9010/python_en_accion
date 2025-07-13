# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 10:47:26 2024

@author: USUARIO
"""

def eliminar_palabra(diccionario: dict, palabra: str) -> bool:
    """
    Esta función elimina una palabra y su definición de un diccionario y retorna True si la palabra
    existe y fue eliminada correctamente, de lo contrario retorna False.
    """
    palabra_eliminada = False

    if palabra in diccionario:
        definicion_eliminada = diccionario.pop(palabra)
        print("Se eliminó la llave", palabra, "que tenía la definición", definicion_eliminada)
        palabra_eliminada = True

    return palabra_eliminada

# Ejemplo de uso
diccionario_palabras = {'hola': 'saludo', 'adios': 'despedida'}
palabra_a_eliminar = 'hola'

if eliminar_palabra(diccionario_palabras, palabra_a_eliminar):
    print(f"La palabra '{palabra_a_eliminar}' fue eliminada correctamente.")
else:
    print(f"La palabra '{palabra_a_eliminar}' no existe en el diccionario.")
