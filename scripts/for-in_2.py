# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:44:09 2024

@author: USUARIO
"""
# Solicitar al usuario que ingrese un número
numero = int(input("Escribe un numero: "))

# Iterar sobre la lista de potencias [2, 3, 4, 5]
for potencia in [2, 3, 4, 5]:
    # Mostrar el número elevado a la potencia actual
    # Nota: El formato correcto debería ser {0} elevado a {1} es {2}, donde {0} se reemplaza por el número,
    # {1} se reemplaza por el exponente y {2} se reemplaza por el resultado de la operación.
    print("{0} elevado a {1} es {2}".format(numero, potencia, numero ** potencia))
