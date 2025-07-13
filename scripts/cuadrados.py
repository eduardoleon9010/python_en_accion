"""
Este módulo contiene funciones para calcular el perímetro y el área de un cuadrado, basado en la longitud de su lado. 
Además, incluye un flujo para solicitar al usuario la longitud del lado de un cuadrado y muestra el perímetro y el 
área correspondientes.
"""

def calcular_perimetro(lado):
    """
    Calcula el perímetro de un cuadrado dado su lado.
    
    Parameters:
    lado (float): Longitud del lado del cuadrado.
    
    Returns:
    float: El perímetro calculado del cuadrado.
    """
    return 4 * lado

def calcular_area(lado):
    """
    Calcula el área de un cuadrado dado su lado.
    
    Parameters:
    lado (float): Longitud del lado del cuadrado.
    
    Returns:
    float: El área calculada del cuadrado.
    """
    return lado ** 2

if __name__ == "__main__":
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    
    perimetro = calcular_perimetro(lado)
    area = calcular_area(lado)
    
    print(f"El perímetro del cuadrado es: {perimetro}")
    print(f"El área del cuadrado es: {area}")
