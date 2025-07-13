# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 08:34:01 2024

@author: USUARIO
"""

def producto_mas_costoso(carrito_compras):
    """
    Retorna el nombre del producto más costoso en el carrito de compras.

    Args:
    - carrito_compras (dict): Un diccionario que contiene los nombres de los productos del carrito de compras como llaves
                               y sus respectivos precios como valores. Todas las llaves están escritas únicamente con letras minúsculas.

    Returns:
    - str: El nombre del artículo más costoso en el carrito de compras. Si el carrito de compras está vacío, retornará la cadena "No hay productos en el carrito".
    """
    # Verificar si el carrito de compras está vacío
    if not carrito_compras:
        return "No hay productos en el carrito"
    
    # Obtener el precio más alto en el carrito de compras
    precio_mas_alto = max(carrito_compras.values())
    
    # Obtener todos los productos con el precio más alto
    productos_mas_costosos = [producto for producto, precio in carrito_compras.items() if precio == precio_mas_alto]
    
    # Retornar el producto más costoso con el nombre alfabéticamente menor
    return min(productos_mas_costosos)

# Ejemplo de uso
if __name__ == "__main__":
    # Carrito de compras
    carrito_compras = {
        "manzanas": 3.99,
        "bananas": 2.99,
        "chocolatinas": 4.99,
        "peras": 3.99
    }

    # Obtener el producto más costoso del carrito de compras
    producto_costoso = producto_mas_costoso(carrito_compras)

    # Mostrar el resultado
    print("El producto más costoso en el carrito de compras es:", producto_costoso)
