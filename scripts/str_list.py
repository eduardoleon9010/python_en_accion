def insertar_ordenado(lista_ordenada: list, cadena: str) -> list:
    """
    Inserta una cadena de manera ordenada en una lista ya ordenada.

    Parámetros:
    lista_ordenada (list): Una lista de cadenas ya ordenada.
    cadena (str): La cadena a insertar en la lista de manera ordenada.

    Retorna:
    list: La lista ordenada con la cadena insertada en su posición correcta.
    """
    i = 0
    while i < len(lista_ordenada) and cadena > lista_ordenada[i]:
        i += 1
    lista_ordenada.insert(i, cadena)
    return lista_ordenada

def ordenar_lista(lista_desordenada: list) -> list:
    """
    Ordena una lista desordenada utilizando el método de inserción ordenada.

    Parámetros:
    lista_desordenada (list): Una lista de cadenas desordenada.

    Retorna:
    list: La lista ordenada resultante.
    """
    ordenada = []
    for cadena in lista_desordenada:
        ordenada = insertar_ordenado(ordenada, cadena)
    return ordenada

# Ejemplo de uso
lista = ["tanque", "avion", "moto", "automovil", "barco", "diligencia"]
orden = ordenar_lista(lista)
print(orden)

