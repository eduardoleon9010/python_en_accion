# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 08:34:40 2024

@author: USUARIO
"""

def valor_carrito_compras(carrito_compras):
    """
    Retorna el valor total del carrito de compras.

    Args:
    - carrito_compras (dict): Un diccionario que contiene los nombres de los productos del carro de compras como llaves
                               y sus respectivos precios como valores.

    Returns:
    - float: Valor total del carro de compras. Si el carro de compras está vacío, retornará el valor cero.
    """
    # Verificar si el carrito de compras está vacío
    if not carrito_compras:
        return 0.0
    
    # Sumar los precios individuales de todos los productos en el carrito
    total = sum(carrito_compras.values())
    
    return total

# Ejemplo de uso
if __name__ == "__main__":
    # Carrito de compras
    carrito_compras = {
        "manzanas": 3.99,
        "bananas": 2.99,
        "chocolatinas": 4.99,
        "peras": 3.99
    }

    # Obtener el valor total del carrito de compras
    valor_total = valor_carrito_compras(carrito_compras)

    # Mostrar el resultado
    print("El valor total del carrito de compras es:", valor_total)
