# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:48:04 2024

@author: USUARIO
"""

def limpiar_diccionario(el_diccionario: dict) -> None:
    """
    Esta función recibe un diccionario como parámetro y utiliza el método 'clear' para eliminar todos
    los elementos del diccionario, dejándolo vacío.

    Parámetros:
    - el_diccionario (dict): Un diccionario que se limpiará. Se pasa por referencia, por lo que los cambios
      realizados dentro de la función afectarán al diccionario original.

    Resultado:
    - None: La función no devuelve nada explícitamente, pero modifica el diccionario proporcionado.
    """
    el_diccionario.clear()

# Ejemplo de uso:
d = {"a": 1, "b": 2, "c": 3}
print("Diccionario antes de la función:", d)
limpiar_diccionario(d)
print("Diccionario después de la función:", d)
