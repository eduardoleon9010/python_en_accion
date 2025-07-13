"""
Encuentra la posición del número más pequeño en una lista.

Esta función, `menor_posicion_lista`, recibe una lista de números y devuelve la posición del número más 
pequeño en la lista.

Args:
- numeros (list): Lista de números enteros.

Returns:
- int: La posición del número más pequeño en la lista.

Ejemplo de uso:
lista = [4, -1, -4, 5, 1, 6, 10, 17, 31, -14, -61]
print(menor_posicion_lista(lista))  # Imprime la posición del número más pequeño.
"""


def menor_posicion_lista(numeros:list) -> int:
    """
    Encuentra la posición del número más pequeño en una lista.

    Args:
    - numeros (list): Lista de números enteros.

    Returns:
    - int: La posición del número más pequeño en la lista.
    """
    indice = 0
    menor = numeros[0]
    
    for i in range(0, len(numeros)):
        if numeros[i] < menor:
            indice = i
            
    return indice

# Ejemplo de uso
lista = [4, -1, -4, 5, 1, 6, 10, 17, 31, -14, -61]
print(menor_posicion_lista(lista))  # Imprime la posición del número más pequeño.

