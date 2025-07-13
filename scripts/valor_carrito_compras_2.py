# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 08:40:06 2024

@author: USUARIO
"""

def valor_carrito_compras(carrito_compras):
    """
    Retorna el valor total del carrito de compras en pesos colombianos.

    Args:
    - carrito_compras (dict): Un diccionario que contiene los nombres de los productos del carro de compras como llaves
                               y sus respectivos precios como valores.

    Returns:
    - str: Valor total del carro de compras en pesos colombianos. Si el carro de compras está vacío, retornará el valor cero.
    """
    # Verificar si el carrito de compras está vacío
    if not carrito_compras:
        return "0.00 COP"
    
    # Sumar los precios individuales de todos los productos en el carrito
    total = sum(carrito_compras.values())

    # Formatear el valor total en pesos colombianos
    valor_en_pesos = "{:,.2f} COP".format(total)
    
    return valor_en_pesos

# Función para solicitar al usuario los productos y sus precios
def ingresar_productos():
    carrito_compras = {}
    while True:
        producto = input("Ingrese el nombre del producto ('fin' para terminar): ").strip().lower()
        if producto == 'fin':
            break
        cantidad = int(input(f"Ingrese la cantidad de '{producto}': "))
        precio = float(input(f"Ingrese el precio de '{producto}' por unidad: "))
        carrito_compras[producto] = cantidad * precio
    return carrito_compras

# Ejemplo de uso
if __name__ == "__main__":
    # Solicitar al usuario los productos y sus precios
    carrito_compras = ingresar_productos()

    # Obtener el valor total del carrito de compras
    valor_total = valor_carrito_compras(carrito_compras)

    # Mostrar el resultado
    print("El valor total del carrito de compras es:", valor_total)
