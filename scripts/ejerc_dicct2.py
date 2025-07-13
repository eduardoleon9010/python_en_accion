"""
Este script resuelve ecuaciones cuadráticas de la forma y = ax**2 + bx + c y las imprime. Utiliza la fórmula 
cuadrática para encontrar las soluciones reales de la ecuación.

solucionar_cuadratica(a, b, c): Esta función toma los coeficientes de una ecuación cuadrática y calcula las 
soluciones reales. Primero, calcula el determinante, y si este es mayor o igual a cero (lo que indica que hay 
soluciones reales), aplica la fórmula cuadrática para encontrar las soluciones.

imprimir_soluciones(soluciones): Imprime las soluciones de una ecuación cuadrática o un mensaje si no hay 
soluciones reales.

El script también incluye ejemplos de uso de estas funciones:

Calcula e imprime las soluciones de una ecuación sin soluciones reales, y muestra un mensaje indicando que no 
hay soluciones reales para esa ecuación.
Calcula e imprime las soluciones de una ecuación con dos soluciones reales diferentes.

"""
import math
def solucionar_cuadratica(a: int, b: int, c:int) -> tuple:
    """ Encuentra las soluciones reales de una ecuación cuadrática de la forma
        y = ax^2 + bx + c
    Parámetros:
      a (int): El coeficiente del término de orden 2
      b (int): El coeficiente del término de orden 1
      c (int): El coeficiente del término de orden 0
    Retorna:
      (tuple): Una tupla con las soluciones reales de la ecuación.
               Retorna None si la ecuación no tiene solución real.
    """
    soluciones = None
    determinante = (b**2) - (4*a*c)
    if determinante >= 0:
        sol1 = -b + (math.sqrt(determinante))
        sol2 = -b - (math.sqrt(determinante))
        soluciones = (sol1, sol2)
    return soluciones

def imprimir_soluciones(soluciones: tuple) -> None:
    """ Imprime las soluciones de una ecuación cuadrática o imprime
        un mensaje indicando que no había soluciones.
    Parámetros:
      soluciones (tuple): Una tupla con dos elementos que son las soluciones de la ecuación.
                          Si no hay soluciones reales, 'soluciones' debe tener el valor None.
    """
    if soluciones is None:
        print("La ecuación no tenía soluciones reales")
    else:
        print("Las soluciones son", soluciones[0], "y", soluciones[1])

# Calcular e imprimir las soluciones de una ecuación sin soluciones reales
soluciones = solucionar_cuadratica(1,1,1)
imprimir_soluciones(soluciones)

# Calcular e imprimir las soluciones de una ecuación con dos soluciones reales diferentes
soluciones = solucionar_cuadratica(1,0,-1)
imprimir_soluciones(soluciones)

