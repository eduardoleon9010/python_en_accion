"""
Este código en Python ilustra varios ejemplos de conversión entre diferentes tipos de datos 
utilizando las funciones int(), float(), y cómo imprimir los resultados.

Este conjunto de conversiones demuestra cómo la función int() convierte números o cadenas en 
enteros, float() convierte a números de punto flotante y str() convierte a cadenas. 
Los resultados se imprimen después de cada conversión para mostrar los tipos de datos resultantes.
"""

# Convierte el número 3.14 a 3
numero_entero = int(3.14)

# Convierte la cadena '-4' a -4
cadena_entero = int('-4')

print(numero_entero)  # Imprime: 3
print(cadena_entero)  # Imprime: -4

# Convierte el número entero 3 a 3.0
numero_decimal = float(3)

# Convierte la cadena '-4.5' a -4.5
cadena_decimal = float('-4.5')

print(numero_decimal)  # Imprime 3.0
print(cadena_decimal)  # Imprime -4.5

# Convierte el número entero 3 a la cadena '3'
entero_cadena = str(3)

# Convierte el número decimal -4.5 a la cadena '-4.5'
decimal_cadena = str(-4.5)

print(entero_cadena)   # Imprime '3'
print(decimal_cadena)  # Imprime '-4.5'
