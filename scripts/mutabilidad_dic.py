"""
Este código en Python define una función modificar que toma un entero y una cadena como entrada, 
incrementa el entero en 100, agrega '!!!!' a la cadena e imprime los valores actualizados. 
Luego llama a la función con un entero y una cadena, y finalmente imprime los valores originales 
de las variables entero y cadena.
"""

def modificar(entero: int, cadena: str) -> bool:
    """
    Modifica los parámetros entero y cadena e imprime sus valores actualizados.
    
    Parámetros:
    entero (int): Un valor entero que se incrementará en 100.
    cadena (str): Una cadena a la que se le añadirá '!!!!'.
    
    Retorna:
    bool: Siempre retorna True.
    """
    entero += 100
    cadena += '!!!!'
    print(entero, cadena)
    return True

numero = 1
texto = "Hola Mundo"
resultado = modificar(numero, texto)
print(numero, texto)
