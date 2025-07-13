
def funcion(p1: str, p2: str, p3: dict, p4: dict) -> None:
    """
    Modifica y compara los valores de las cadenas y diccionarios recibidos como argumentos.

    Parámetros:
    p1 (str): Una cadena inicial.
    p2 (str): Una cadena inicial idéntica a p1.
    p3 (dict): Un diccionario inicial.
    p4 (dict): Un diccionario inicial idéntico a p3.

    La función imprime y compara los valores recibidos, luego modifica algunos de los parámetros.
    Se realizan modificaciones a p1 y p3, y se intenta reasignar p3 a un nuevo diccionario.
    Finalmente, muestra los valores modificados y comprueba si las variables iniciales se han modificado.

    Retorna:
    None
    """
    print("--> Valores recibidos:", p1, p2, p3, p4)
    print("--> Comparar las cadenas:", p1 == p2)
    print("--> Comparar los diccionarios:", p3 == p4, p3 is p4)
    
    p1 = "nueva cadena"
    p3["nuevo valor"] = 99
    print("--> Valores modificados:", p1, p2, p3, p4)
    p3 = {"ultimo": 1}
    print("--> Valores modificados de nuevo:", p3, p4)    

cadena = "cadena inicial"
diccionario = {"inicial": 0}

print("Antes de llamar a la función: ", cadena, diccionario)
funcion(cadena, cadena, diccionario, diccionario)
print("Después de llamar a la función: ", cadena, diccionario)
