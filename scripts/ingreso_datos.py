"""
Este código realiza lo siguiente:

Solicita al usuario que introduzca el valor de 'a'.
Lee la entrada del usuario para 'a' y almacena este valor.
Solicita al usuario que introduzca el valor de 'b'.
Lee la entrada del usuario para 'b' y almacena este valor.
Convierte los valores de 'a' y 'b' a números flotantes.
Realiza la suma de los valores de 'a' y 'b'.
Imprime el resultado de la suma en la consola.
El código solicita dos valores al usuario ('a' y 'b'), 
los suma y muestra el resultado de la suma en la consola.
"""

print('Introduzca el valor a: ')
valor_a = input()

print('Introduzca el valor b: ')
valor_b = input()

resultado = float(valor_a) + float(valor_b)

print(resultado)
