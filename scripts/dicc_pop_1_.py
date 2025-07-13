# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 10:42:40 2024

@author: USUARIO
"""

# Documentación del código:

# Diccionario de ejemplo
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Verificar si la clave 'b' existe antes de eliminarla
clave_a_eliminar = 'b'
if clave_a_eliminar in mi_diccionario:
    # Utilizar el método pop para eliminar la clave 'b' y obtener su valor
    valor_eliminado = mi_diccionario.pop(clave_a_eliminar)
    # Imprimir mensaje indicando la eliminación exitosa
    print(f"Se eliminó la clave '{clave_a_eliminar}' con el valor {valor_eliminado}")
else:
    # Imprimir mensaje indicando que la clave no existe en el diccionario
    print(f"La clave '{clave_a_eliminar}' no existe en el diccionario")

# Imprimir el diccionario actualizado
print("Diccionario actualizado:", mi_diccionario)
