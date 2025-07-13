"""
Este código define una función area_cuadrado que solicita al usuario ingresar la longitud del lado del cuadrado. 
Luego, calcula el área del cuadrado y la devuelve. Por último, se imprime el área del cuadrado ingresado por el usuario.
"""

def area_cuadrado() -> int:
    """
    Calcula el área de un cuadrado dada la medida de su lado ingresada por el usuario.
    
    Returns:
    int: El área calculada del cuadrado.
    """
    lado = int(input("Ingrese la longitud del lado del cuadrado: "))
    return lado * lado

# Solicitar al usuario la longitud del lado y mostrar el área del cuadrado
area = area_cuadrado()
print("El área del cuadrado es:", area)
