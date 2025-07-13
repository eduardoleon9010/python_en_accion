"""
Identificador de Números Pares e Impares
Descripción
Este script en Python solicita al usuario que ingrese un número y determina si es par o impar. 
Dependiendo de la paridad del número ingresado, muestra un mensaje adicional con información 
relacionada con la naturaleza de los números pares o impares
"""
x = int(input("Digite un número: "))

if x % 2 == 0:
     print(x, "es par")
     print("¿Sabía usted que 2 es el único número que es primo?")
else:
    print(x, "es impar")
    print("¿Sabía usted que multiplicar dos números impares siempre da un resultado impar?")

"""
Funcionamiento del Código
Solicita al usuario que ingrese un número.
Verifica si el número es par o impar utilizando la operación módulo (%).
Muestra un mensaje correspondiente a la paridad del número ingresado.

Uso y Notas Adicionales
Este script es una manera simple de identificar si un número es par o impar y compartir 
información interesante relacionada con la naturaleza matemática de los números pares e impares.
"""
