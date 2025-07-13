"""
Esta función utiliza la biblioteca math de Python para acceder al valor de π (pi) y luego 
calcula el área del círculo utilizando la fórmula mencionada.

"""

import math

def area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo dado su radio.

    Parameters:
    radio (float): El radio del círculo.

    Returns:
    float: El área calculada del círculo.
    """
    return math.pi * radio ** 2
