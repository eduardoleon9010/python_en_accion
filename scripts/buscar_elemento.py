# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 08:20:22 2024

@author: USUARIO
"""

def buscar_elemento(entrada, buscado):
    """
    Busca el índice de un elemento en una lista.

    Parámetros:
    - entrada (list): Lista en la que se buscará el número.
    - buscado (int): Número entero a buscar.

    Retorna:
    - int: Índice del elemento buscado en la lista. Retorna -1 si no se encuentra.
    """
    try:
        # Utilizamos el método index() para buscar el elemento en la lista.
        indice = entrada.index(buscado)
        return indice
    except ValueError:
        # Si el elemento no se encuentra, se maneja la excepción y se retorna -1.
        return -1

# Ejemplo de uso:
lista_ejemplo = [5, 10, 15, 20, 25]
numero_buscado = 15

# Llamamos a la función e imprimimos el resultado.
resultado = buscar_elemento(lista_ejemplo, numero_buscado)
print(f"El número {numero_buscado} se encuentra en el índice {resultado}")
